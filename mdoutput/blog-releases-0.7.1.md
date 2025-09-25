<!-- Source: https://docs.crawl4ai.com/blog/releases/0.7.1/ -->

[Crawl4AI Documentation (v0.7.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/0.7.1/)


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
  * [🛠️ Crawl4AI v0.7.1: Minor Cleanup Update](https://docs.crawl4ai.com/blog/releases/0.7.1/#crawl4ai-v071-minor-cleanup-update)
  * [🎯 What's Changed](https://docs.crawl4ai.com/blog/releases/0.7.1/#whats-changed)
  * [🧹 Code Cleanup](https://docs.crawl4ai.com/blog/releases/0.7.1/#code-cleanup)
  * [📖 Documentation Updates](https://docs.crawl4ai.com/blog/releases/0.7.1/#documentation-updates)
  * [🚀 Installation](https://docs.crawl4ai.com/blog/releases/0.7.1/#installation)


# 🛠️ Crawl4AI v0.7.1: Minor Cleanup Update
_July 17, 2025 • 2 min read_
* * *
A small maintenance release that removes unused code and improves documentation.
## 🎯 What's Changed
  * **Removed unused StealthConfig** from `crawl4ai/browser_manager.py`
  * **Updated documentation** with better examples and parameter explanations
  * **Fixed virtual scroll configuration** examples in docs


## 🧹 Code Cleanup
Removed unused `StealthConfig` import and configuration that wasn't being used anywhere in the codebase. The project uses its own custom stealth implementation through JavaScript injection instead.
```
# Removed unused code:
from playwright_stealth import StealthConfig
stealth_config = StealthConfig(...)  # This was never used
Copy
```

## 📖 Documentation Updates
  * Fixed adaptive crawling parameter examples
  * Updated session management documentation
  * Corrected virtual scroll configuration examples


## 🚀 Installation
```
pip install crawl4ai==0.7.1
Copy
```

No breaking changes - upgrade directly from v0.7.0.
* * *
Questions? Issues? - GitHub: [github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) - Discord: [discord.gg/crawl4ai](https://discord.gg/jP8KfhDhyN)
#### On this page
  * [🎯 What's Changed](https://docs.crawl4ai.com/blog/releases/0.7.1/#whats-changed)
  * [🧹 Code Cleanup](https://docs.crawl4ai.com/blog/releases/0.7.1/#code-cleanup)
  * [📖 Documentation Updates](https://docs.crawl4ai.com/blog/releases/0.7.1/#documentation-updates)
  * [🚀 Installation](https://docs.crawl4ai.com/blog/releases/0.7.1/#installation)


* * *
> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")
