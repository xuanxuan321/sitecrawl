# pip install -U crawl4ai
import asyncio, time, xml.etree.ElementTree as ET
from crawl4ai import AsyncUrlSeeder, SeedingConfig, AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy

DOMAIN = "ant-design.antgroup.com"   # 只写域名，如 react.dev

async def discover_urls(domain: str) -> list[str]:
    # 1) 先用 URL 播种从 sitemap 获取（支持 sitemap 索引）
    try:
        async with AsyncUrlSeeder() as seeder:
            cfg = SeedingConfig(source="sitemap", extract_head=False, live_check=True)
            rows = await seeder.urls(domain, cfg)  # rows: [{"url": "...", "status": "valid", ...}, ...]
            urls = [r["url"] for r in rows if r.get("status") in (None, "valid")]
            if urls:
                return sorted(set(urls))
    except Exception:
        pass

    # 2) 回退：用 BFS 在站内最多爬 2 层把 URL 发现出来
    async with AsyncWebCrawler() as crawler:
        config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=5, include_external=False, max_pages=1000),
            only_text=True,
        )
        results = await crawler.arun(f"https://{domain}", config=config)
        return sorted({r.url for r in results if getattr(r, "success", False)})

def write_sitemap(urls: list[str], out_path="sitemap.xml"):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    today = time.strftime("%Y-%m-%d")
    for u in urls:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = u
        ET.SubElement(url, "lastmod").text = today
    ET.ElementTree(urlset).write(out_path, encoding="utf-8", xml_declaration=True)

def analyze_sitemap(urls: list[str], domain: str):
    """分析网站地图并输出统计信息"""
    print(f"\n📊 网站分析报告 - {domain}")
    print("=" * 50)
    print(f"总共发现 {len(urls)} 个页面")
    
    # 按路径分类统计
    categories = {}
    for url in urls:
        # 移除域名部分，获取路径
        path_part = url.replace(f"https://{domain}", "").replace(f"http://{domain}", "")
        if not path_part or path_part == "/" or path_part == "":
            category = "home"
        else:
            # 获取第一级路径作为分类
            path_parts = path_part.strip("/").split("/")
            category = path_parts[0] if path_parts[0] else "home"
        
        categories[category] = categories.get(category, 0) + 1
    
    print(f"\n📂 主要页面分类:")
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count} 页面")
    
    # 显示一些示例URL
    print(f"\n🔗 示例页面:")
    for i, url in enumerate(urls[:5]):
        print(f"  {i+1}. {url}")
    
    if len(urls) > 5:
        print(f"  ... 还有 {len(urls) - 5} 个页面")
    
    print(f"\n✅ 网站地图已保存到: sitemap.xml")

async def main():
    urls = await discover_urls(DOMAIN)
    write_sitemap(urls)
    print(f"Got {len(urls)} urls → sitemap.xml")
    
    # 分析并输出统计信息
    analyze_sitemap(urls, DOMAIN)

if __name__ == "__main__":
    asyncio.run(main())