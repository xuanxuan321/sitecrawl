<!-- Source: https://docs.crawl4ai.com/migration/webscraping-strategy-migration/ -->

[Crawl4AI Documentation (v0.7.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/)


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
  * [WebScrapingStrategy Migration Guide](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#webscrapingstrategy-migration-guide)
  * [Overview](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#overview)
  * [What Changed?](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#what-changed)
  * [Backward Compatibility](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#backward-compatibility)
  * [Migration Options](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#migration-options)
  * [Type Hints](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#type-hints)
  * [Subclassing](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#subclassing)
  * [Performance Benefits](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#performance-benefits)
  * [Summary](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#summary)


# WebScrapingStrategy Migration Guide
## Overview
Crawl4AI has simplified its content scraping architecture. The BeautifulSoup-based `WebScrapingStrategy` has been deprecated in favor of the faster LXML-based implementation. However, **no action is required** - your existing code will continue to work.
## What Changed?
  1. **`WebScrapingStrategy`is now an alias** for `LXMLWebScrapingStrategy`
  2. **The BeautifulSoup implementation has been removed** (~1000 lines of redundant code)
  3. **`LXMLWebScrapingStrategy`inherits directly** from `ContentScrapingStrategy`
  4. **Performance remains optimal** with LXML as the sole implementation


## Backward Compatibility
**Your existing code continues to work without any changes:**
```
# This still works perfectly
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, WebScrapingStrategy

config = CrawlerRunConfig(
    scraping_strategy=WebScrapingStrategy()  # Works as before
)
Copy
```

## Migration Options
You have three options:
### Option 1: Do Nothing (Recommended)
Your code will continue to work. `WebScrapingStrategy` is permanently aliased to `LXMLWebScrapingStrategy`.
### Option 2: Update Imports (Optional)
For clarity, you can update your imports:
```
# Old (still works)
from crawl4ai import WebScrapingStrategy
strategy = WebScrapingStrategy()

# New (more explicit)
from crawl4ai import LXMLWebScrapingStrategy
strategy = LXMLWebScrapingStrategy()
Copy
```

### Option 3: Use Default Configuration
Since `LXMLWebScrapingStrategy` is the default, you can omit the strategy parameter:
```
# Simplest approach - uses LXMLWebScrapingStrategy by default
config = CrawlerRunConfig()
Copy
```

## Type Hints
If you use type hints, both work:
```
from crawl4ai import WebScrapingStrategy, LXMLWebScrapingStrategy

def process_with_strategy(strategy: WebScrapingStrategy) -> None:
    # Works with both WebScrapingStrategy and LXMLWebScrapingStrategy
    pass

# Both are valid
process_with_strategy(WebScrapingStrategy())
process_with_strategy(LXMLWebScrapingStrategy())
Copy
```

## Subclassing
If you've subclassed `WebScrapingStrategy`, it continues to work:
```
class MyCustomStrategy(WebScrapingStrategy):
    def __init__(self):
        super().__init__()
        # Your custom code
Copy
```

## Performance Benefits
By consolidating to LXML: - **10-20x faster** HTML parsing for large documents - **Lower memory usage** - **Consistent behavior** across all use cases - **Simplified maintenance** and bug fixes
## Summary
This change simplifies Crawl4AI's internals while maintaining 100% backward compatibility. Your existing code continues to work, and you get better performance automatically.
#### On this page
  * [Overview](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#overview)
  * [What Changed?](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#what-changed)
  * [Backward Compatibility](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#backward-compatibility)
  * [Migration Options](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#migration-options)
  * [Option 1: Do Nothing (Recommended)](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#option-1-do-nothing-recommended)
  * [Option 2: Update Imports (Optional)](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#option-2-update-imports-optional)
  * [Option 3: Use Default Configuration](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#option-3-use-default-configuration)
  * [Type Hints](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#type-hints)
  * [Subclassing](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#subclassing)
  * [Performance Benefits](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#performance-benefits)
  * [Summary](https://docs.crawl4ai.com/migration/webscraping-strategy-migration/#summary)


* * *
> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")
