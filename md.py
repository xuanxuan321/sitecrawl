import asyncio
import re
import sys
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse
import xml.etree.ElementTree as ET

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

SITEMAP_PATH = Path("sitemap.xml")
OUTPUT_DIR = Path("mdoutput")


def load_urls_from_sitemap(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(f"Sitemap not found: {path}")

    tree = ET.parse(path)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    for loc in tree.findall(".//sm:loc", namespace):
        if loc.text:
            url = loc.text.strip()
            if url:
                urls.append(url)
    return urls


def safe_filename_for_url(url: str, used: set[str]) -> Path:
    parsed = urlparse(url)
    path = unquote(parsed.path or "")
    # Collapse path segments into a slug
    parts = [segment for segment in re.split(r"[\\/]+", path.strip("/")) if segment]
    if not parts:
        parts = ["index"]
    slug = "-".join(parts)

    if parsed.query:
        query_slug = re.sub(r"[^A-Za-z0-9]+", "-", parsed.query)
        if query_slug:
            slug = f"{slug}-{query_slug.strip('-')}"

    slug = re.sub(r"[^A-Za-z0-9._-]", "-", slug).strip("-_.") or "page"

    candidate = slug
    counter = 2
    while candidate in used:
        candidate = f"{slug}-{counter}"
        counter += 1
    used.add(candidate)
    return OUTPUT_DIR / f"{candidate}.md"


def extract_markdown(result) -> str:
    candidate_attrs = (
        "markdown",
        "markdown_v2",
        "markdown_v3",
        "markdown_v2_raw",
        "fit_markdown",
        "page_markdown",
        "clean_markdown",
        "text_content",
        "text",
        "content",
    )

    for attr in candidate_attrs:
        value = getattr(result, attr, None)
        if isinstance(value, str) and value.strip():
            return value

    # Some versions expose nested dictionaries
    for attr in ("data", "extracted", "extracted_content"):
        payload = getattr(result, attr, None)
        if isinstance(payload, dict):
            for key in ("markdown", "markdown_v2", "text"):
                value = payload.get(key)
                if isinstance(value, str) and value.strip():
                    return value

    return ""


async def crawl_and_write(urls: Iterable[str]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    used_names: set[str] = set()
    config = CrawlerRunConfig()

    async with AsyncWebCrawler() as crawler:
        for index, url in enumerate(urls, start=1):
            target_path = safe_filename_for_url(url, used_names)
            print(f"[{index}/{len(urls)}] Crawling {url} → {target_path.name}")

            try:
                results = await crawler.arun(url, config=config)
            except Exception as exc:  # pragma: no cover - network / runtime errors
                print(f"  ✗ Failed to crawl {url}: {exc}")
                continue

            if not results:
                print(f"  ✗ No results returned for {url}")
                continue

            # Some crawler strategies return multiple items; grab the one matching the URL
            result = next((item for item in results if getattr(item, "url", "") == url), results[0])
            if not getattr(result, "success", True):
                reason = getattr(result, "error_message", "unknown error")
                print(f"  ✗ Crawl reported failure: {reason}")
                continue

            markdown = extract_markdown(result)
            if not markdown:
                print(f"  ✗ No markdown extracted for {url}")
                continue

            content = f"<!-- Source: {url} -->\n\n{markdown.strip()}\n"
            target_path.write_text(content, encoding="utf-8")
            print(f"  ✓ Saved to {target_path}")


async def async_main() -> None:
    urls = load_urls_from_sitemap(SITEMAP_PATH)
    if not urls:
        print("No URLs found in sitemap. Nothing to do.")
        return

    await crawl_and_write(urls)


def main() -> None:
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:  # pragma: no cover
        sys.exit(1)


if __name__ == "__main__":
    main()
