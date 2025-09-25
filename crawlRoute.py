"""Path-scoped crawler using crawl4ai, with in-process BFS that never explores
links outside the requested base path. Only links under the specified path are
queued, so out-of-scope routes are never visited."""

import asyncio
import re
from collections import deque
from typing import Iterable
from urllib.parse import urlparse, urlunparse, urljoin

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl import write_sitemap, analyze_sitemap


# 目标可以包含路径，例如 "docs.crawl4ai.com/advanced"
TARGET = "ant-design.antgroup.com/components"


def _normalize_target(target: str) -> tuple[str, str, str]:
    """拆分目标字符串，返回 (scheme, netloc, base_path)。"""

    if not target or target.isspace():
        raise ValueError("TARGET 不能为空")

    candidate = target.strip()
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", candidate):
        candidate = f"https://{candidate}"

    parsed = urlparse(candidate)
    if not parsed.netloc:
        raise ValueError(f"无法解析目标主机名: {target}")

    scheme = parsed.scheme or "https"
    netloc = parsed.netloc
    path = parsed.path or "/"
    if not path.startswith("/"):
        path = f"/{path}"

    normalized_path = "/" if path == "/" else f"/{path.strip('/')}"
    return scheme, netloc, normalized_path


def _normalize_path(path: str) -> str:
    """将路径标准化：移除多余斜杠与结尾斜杠（根路径除外）。"""
    if not path:
        return "/"
    if not path.startswith("/"):
        path = f"/{path}"
    cleaned = "/".join([p for p in path.split("/") if p])
    return "/" if cleaned == "" else f"/{cleaned}"


def _url_allows(url: str, scheme: str, netloc: str, base_path: str) -> bool:
    """基于完整 URL 判断是否允许：限定同域且在 base_path 子树内。"""
    try:
        parsed = urlparse(url)
    except Exception:
        return False

    # 仅允许 http/https 同域
    if parsed.scheme not in ("http", "https"):
        return False
    if parsed.netloc.lower() != netloc.lower():
        return False

    candidate_path = _normalize_path(parsed.path)
    base = _normalize_path(base_path)

    if base == "/":
        return True

    if candidate_path == base:
        return True

    return candidate_path.startswith(base + "/")


def _collect_links_from_result(result) -> Iterable[str]:
    """Best-effort extraction of outgoing links from a crawl4ai result."""
    candidates = []

    # Common attributes where links might be exposed
    for attr in (
        "links",
        "all_links",
        "outgoing_urls",
        "extracted_urls",
        "urls",
        "a_hrefs",
        "hrefs",
    ):
        value = getattr(result, attr, None)
        if isinstance(value, (list, tuple, set)):
            candidates.extend([str(x) for x in value])

    # Try nested dict payloads
    for attr in ("data", "extracted", "extracted_content"):
        payload = getattr(result, attr, None)
        if isinstance(payload, dict):
            for key in ("links", "urls", "outgoing_urls"):
                value = payload.get(key)
                if isinstance(value, (list, tuple, set)):
                    candidates.extend([str(x) for x in value])

    # As a final fallback, regex from HTML/text
    html = (
        getattr(result, "html", None)
        or getattr(result, "raw_html", None)
        or getattr(result, "page_html", None)
        or getattr(result, "content_html", None)
        or getattr(result, "content", None)
    )
    if isinstance(html, str) and "href" in html:
        for m in re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, flags=re.I):
            candidates.append(m)

    # Dedup while preserving order
    seen = set()
    result_links = []
    for u in candidates:
        if u not in seen:
            seen.add(u)
            result_links.append(u)
    return result_links


async def discover_route_urls(target: str) -> tuple[list[str], str]:
    """Run a BFS limited to base_path; never enqueue out-of-scope links."""
    scheme, netloc, base_path = _normalize_target(target)
    start_url = f"{scheme}://{netloc}{base_path}"

    config = CrawlerRunConfig(only_text=False)

    visited: set[str] = set()
    discovered: list[str] = []
    q: deque[tuple[str, int]] = deque([(start_url, 0)])
    MAX_DEPTH = 1


    async with AsyncWebCrawler() as crawler:
        while q:
            url, depth = q.popleft()
            if url in visited:
                continue
            visited.add(url)

            try:
                results = await crawler.arun(url, config=config)
            except Exception:
                continue

            # crawl4ai may return multiple items; keep the one that matches
            result = None
            if isinstance(results, (list, tuple)) and results:
                for item in results:
                    if getattr(item, "url", "") == url:
                        result = item
                        break
                if result is None:
                    result = results[0]
            else:
                result = results

            if not getattr(result, "success", True):
                continue

            # Record this page when in scope
            if _url_allows(url, scheme, netloc, base_path):
                discovered.append(url)

            # Stop expanding if depth reached
            if depth >= MAX_DEPTH:
                continue

            # Extract and enqueue only allowed links
            for href in _collect_links_from_result(result):
                abs_url = urljoin(url, href)
                if _url_allows(abs_url, scheme, netloc, base_path) and abs_url not in visited:
                    q.append((abs_url, depth + 1))

    return sorted(set(discovered)), netloc


async def main_async() -> None:
    urls, netloc = await discover_route_urls(TARGET)
    write_sitemap(urls)
    print(f"Got {len(urls)} urls → sitemap.xml")
    analyze_sitemap(urls, netloc)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
