<!-- Source: https://docs.crawl4ai.com/blog/releases/v0.4.3b1/ -->

[Crawl4AI Documentation (v0.7.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/)


[ unclecode/crawl4ai ](https://github.com/unclecode/crawl4ai)
×
  * [Home](https://docs.crawl4ai.com/)
  * [Ask AI](https://docs.crawl4ai.com/core/ask-ai/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * [Code Examples](https://docs.crawl4ai.com/core/examples/)
  * Apps
    * [Demo Apps](https://docs.crawl4ai.com/apps/)
    * [C4A-Script Editor](https://docs.crawl4ai.com/apps/c4a-script/)
    * [LLM Context Builder](https://docs.crawl4ai.com/apps/llmtxt/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Adaptive Crawling](https://docs.crawl4ai.com/core/adaptive-crawling/)
    * [URL Seeding](https://docs.crawl4ai.com/core/url-seeding/)
    * [C4A-Script](https://docs.crawl4ai.com/core/c4a-script/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [Adaptive Strategies](https://docs.crawl4ai.com/advanced/adaptive-strategies/)
    * [Virtual Scroll](https://docs.crawl4ai.com/advanced/virtual-scroll/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Undetected Browser](https://docs.crawl4ai.com/advanced/undetected-browser/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
    * [Network & Console Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)
    * [PDF Parsing](https://docs.crawl4ai.com/advanced/pdf-parsing/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)
    * [C4A-Script Reference](https://docs.crawl4ai.com/api/c4a-script-reference/)


* * *
  * [Crawl4AI 0.4.3: Major Performance Boost & LLM Integration](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#crawl4ai-043-major-performance-boost-llm-integration)
  * [⚡ Speed & Efficiency Improvements](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#speed-efficiency-improvements)
  * [🤖 LLM Integration](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#llm-integration)
  * [🔧 Core Improvements](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#core-improvements)
  * [Performance Impact](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#performance-impact)
  * [Getting Started](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#getting-started)
  * [Stay Connected](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#stay-connected)


# Crawl4AI 0.4.3: Major Performance Boost & LLM Integration
We're excited to announce Crawl4AI 0.4.3, focusing on three key areas: Speed & Efficiency, LLM Integration, and Core Platform Improvements. This release significantly improves crawling performance while adding powerful new LLM-powered features.
## ⚡ Speed & Efficiency Improvements
### 1. Memory-Adaptive Dispatcher System
The new dispatcher system provides intelligent resource management and real-time monitoring:
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DisplayMode
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher, CrawlerMonitor

async def main():
    urls = ["https://example1.com", "https://example2.com"] * 50

    # Configure memory-aware dispatch
    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=80.0,  # Auto-throttle at 80% memory
        check_interval=0.5,             # Check every 0.5 seconds
        max_session_permit=20,          # Max concurrent sessions
        monitor=CrawlerMonitor(         # Real-time monitoring
            display_mode=DisplayMode.DETAILED
        )
    )

    async with AsyncWebCrawler() as crawler:
        results = await dispatcher.run_urls(
            urls=urls,
            crawler=crawler,
            config=CrawlerRunConfig()
        )
Copy
```

### 2. Streaming Support
Process crawled URLs in real-time instead of waiting for all results:
```
config = CrawlerRunConfig(stream=True)

async with AsyncWebCrawler() as crawler:
    async for result in await crawler.arun_many(urls, config=config):
        print(f"Got result for {result.url}")
        # Process each result immediately
Copy
```

### 3. LXML-Based Scraping
New LXML scraping strategy offering up to 20x faster parsing:
```
config = CrawlerRunConfig(
    scraping_strategy=LXMLWebScrapingStrategy(),
    cache_mode=CacheMode.ENABLED
)
Copy
```

## 🤖 LLM Integration
### 1. LLM-Powered Markdown Generation
Smart content filtering and organization using LLMs:
```
config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(
        content_filter=LLMContentFilter(
            provider="openai/gpt-4o",
            instruction="Extract technical documentation and code examples"
        )
    )
)
Copy
```

### 2. Automatic Schema Generation
Generate extraction schemas instantly using LLMs instead of manual CSS/XPath writing:
```
schema = JsonCssExtractionStrategy.generate_schema(
    html_content,
    schema_type="CSS",
    query="Extract product name, price, and description"
)
Copy
```

## 🔧 Core Improvements
### 1. Proxy Support & Rotation
Integrated proxy support with automatic rotation and verification:
```
config = CrawlerRunConfig(
    proxy_config={
        "server": "http://proxy:8080",
        "username": "user",
        "password": "pass"
    }
)
Copy
```

### 2. Robots.txt Compliance
Built-in robots.txt support with SQLite caching:
```
config = CrawlerRunConfig(check_robots_txt=True)
result = await crawler.arun(url, config=config)
if result.status_code == 403:
    print("Access blocked by robots.txt")
Copy
```

### 3. URL Redirection Tracking
Track final URLs after redirects:
```
result = await crawler.arun(url)
print(f"Initial URL: {url}")
print(f"Final URL: {result.redirected_url}")
Copy
```

## Performance Impact
  * Memory usage reduced by up to 40% with adaptive dispatcher
  * Parsing speed increased up to 20x with LXML strategy
  * Streaming reduces memory footprint for large crawls by ~60%


## Getting Started
```
pip install -U crawl4ai
Copy
```

For complete examples, check our [demo repository](https://github.com/unclecode/crawl4ai/examples).
## Stay Connected
  * Star us on [GitHub](https://github.com/unclecode/crawl4ai)
  * Follow [@unclecode](https://twitter.com/unclecode)
  * Join our [Discord](https://discord.gg/crawl4ai)


Happy crawling! 🕷️
#### On this page
  * [⚡ Speed & Efficiency Improvements](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#speed-efficiency-improvements)
  * [1. Memory-Adaptive Dispatcher System](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#1-memory-adaptive-dispatcher-system)
  * [2. Streaming Support](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#2-streaming-support)
  * [3. LXML-Based Scraping](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#3-lxml-based-scraping)
  * [🤖 LLM Integration](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#llm-integration)
  * [1. LLM-Powered Markdown Generation](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#1-llm-powered-markdown-generation)
  * [2. Automatic Schema Generation](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#2-automatic-schema-generation)
  * [🔧 Core Improvements](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#core-improvements)
  * [1. Proxy Support & Rotation](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#1-proxy-support-rotation)
  * [2. Robots.txt Compliance](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#2-robotstxt-compliance)
  * [3. URL Redirection Tracking](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#3-url-redirection-tracking)
  * [Performance Impact](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#performance-impact)
  * [Getting Started](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#getting-started)
  * [Stay Connected](https://docs.crawl4ai.com/blog/releases/v0.4.3b1/#stay-connected)


* * *
> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")
