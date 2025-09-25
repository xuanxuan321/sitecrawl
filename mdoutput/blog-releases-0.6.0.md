<!-- Source: https://docs.crawl4ai.com/blog/releases/0.6.0/ -->

[Crawl4AI Documentation (v0.7.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/0.6.0/)


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
  * [Crawl4AI v0.6.0 Release Notes](https://docs.crawl4ai.com/blog/releases/0.6.0/#crawl4ai-v060-release-notes)
  * [Highlights](https://docs.crawl4ai.com/blog/releases/0.6.0/#highlights)
  * [Core Improvements](https://docs.crawl4ai.com/blog/releases/0.6.0/#core-improvements)
  * [Breaking Changes & Deprecations](https://docs.crawl4ai.com/blog/releases/0.6.0/#breaking-changes-deprecations)
  * [Miscellaneous Updates](https://docs.crawl4ai.com/blog/releases/0.6.0/#miscellaneous-updates)
  * [New Examples Included](https://docs.crawl4ai.com/blog/releases/0.6.0/#new-examples-included)
  * [Watch the Release Video](https://docs.crawl4ai.com/blog/releases/0.6.0/#watch-the-release-video)
  * [Join the Community](https://docs.crawl4ai.com/blog/releases/0.6.0/#join-the-community)
  * [Install or Upgrade](https://docs.crawl4ai.com/blog/releases/0.6.0/#install-or-upgrade)


# Crawl4AI v0.6.0 Release Notes
We're excited to announce the release of **Crawl4AI v0.6.0** , our biggest and most feature-rich update yet. This version introduces major architectural upgrades, brand-new capabilities for geo-aware crawling, high-efficiency scraping, and real-time streaming support for scalable deployments.
* * *
## Highlights
### 1. **World-Aware Crawlers**
Crawl as if you’re anywhere in the world. With v0.6.0, each crawl can simulate: - Specific GPS coordinates - Browser locale - Timezone
Example: 
```
CrawlerRunConfig(
    url="https://browserleaks.com/geo",
    locale="en-US",
    timezone_id="America/Los_Angeles",
    geolocation=GeolocationConfig(
        latitude=34.0522,
        longitude=-118.2437,
        accuracy=10.0
    )
)
Copy
```

Great for accessing region-specific content or testing global behavior.
* * *
### 2. **Native Table Extraction**
Extract HTML tables directly into usable formats like Pandas DataFrames or CSV with zero parsing hassle. All table data is available under `result.media["tables"]`.
Example: 
```
raw_df = pd.DataFrame(
    result.media["tables"][0]["rows"],
    columns=result.media["tables"][0]["headers"]
)
Copy
```

This makes it ideal for scraping financial data, pricing pages, or anything tabular.
* * *
### 3. **Browser Pooling & Pre-Warming**
We've overhauled browser management. Now, multiple browser instances can be pooled and pages pre-warmed for ultra-fast launches: - Reduces cold-start latency - Lowers memory spikes - Enhances parallel crawling stability
This powers the new **Docker Playground** experience and streamlines heavy-load crawling.
* * *
### 4. **Traffic & Snapshot Capture**
Need full visibility? You can now capture: - Full network traffic logs - Console output - MHTML page snapshots for post-crawl audits and debugging
No more guesswork on what happened during your crawl.
* * *
### 5. **MCP API and Streaming Support**
We’re exposing **MCP socket and SSE endpoints** , allowing: - Live streaming of crawl results - Real-time integration with agents or frontends - A new Playground UI for interactive crawling
This is a major step towards making Crawl4AI real-time ready.
* * *
### 6. **Stress-Test Framework**
Want to test performance under heavy load? v0.6.0 includes a new memory stress-test suite that supports 1,000+ URL workloads. Ideal for: - Load testing - Performance benchmarking - Validating memory efficiency
* * *
## Core Improvements
  * Robots.txt compliance
  * Proxy rotation support
  * Improved URL normalization and session reuse
  * Shared data across crawler hooks
  * New page routing logic


* * *
## Breaking Changes & Deprecations
  * Legacy `crawl4ai/browser/*` modules are removed. Update imports accordingly.
  * `AsyncPlaywrightCrawlerStrategy.get_page` now uses a new function signature.
  * Deprecated markdown generator aliases now point to `DefaultMarkdownGenerator` with warning.


* * *
## Miscellaneous Updates
  * FastAPI validators replaced custom validation logic
  * Docker build now based on a Chromium layer
  * Repo-wide cleanup: ~36,000 insertions, ~5,000 deletions


* * *
## New Examples Included
  * Geo-location crawling
  * Network + console log capture
  * Docker MCP API usage
  * Markdown selector usage
  * Crypto project data extraction


* * *
## Watch the Release Video
Want a visual walkthrough of all these updates? Watch the video: 🔗 https://youtu.be/9x7nVcjOZks
If you're new to Crawl4AI, start here: 🔗 https://www.youtube.com/watch?v=xo3qK6Hg9AA&t=15s
* * *
## Join the Community
We’ve just opened up our **Discord** for the public. Join us to: - Ask questions - Share your projects - Get help or contribute
💬 https://discord.gg/wpYFACrHR4
* * *
## Install or Upgrade
```
pip install -U crawl4ai
Copy
```

* * *
Live long and import crawl4ai. 🖖
#### On this page
  * [Highlights](https://docs.crawl4ai.com/blog/releases/0.6.0/#highlights)
  * [1. World-Aware Crawlers](https://docs.crawl4ai.com/blog/releases/0.6.0/#1-world-aware-crawlers)
  * [2. Native Table Extraction](https://docs.crawl4ai.com/blog/releases/0.6.0/#2-native-table-extraction)
  * [3. Browser Pooling & Pre-Warming](https://docs.crawl4ai.com/blog/releases/0.6.0/#3-browser-pooling-pre-warming)
  * [4. Traffic & Snapshot Capture](https://docs.crawl4ai.com/blog/releases/0.6.0/#4-traffic-snapshot-capture)
  * [5. MCP API and Streaming Support](https://docs.crawl4ai.com/blog/releases/0.6.0/#5-mcp-api-and-streaming-support)
  * [6. Stress-Test Framework](https://docs.crawl4ai.com/blog/releases/0.6.0/#6-stress-test-framework)
  * [Core Improvements](https://docs.crawl4ai.com/blog/releases/0.6.0/#core-improvements)
  * [Breaking Changes & Deprecations](https://docs.crawl4ai.com/blog/releases/0.6.0/#breaking-changes-deprecations)
  * [Miscellaneous Updates](https://docs.crawl4ai.com/blog/releases/0.6.0/#miscellaneous-updates)
  * [New Examples Included](https://docs.crawl4ai.com/blog/releases/0.6.0/#new-examples-included)
  * [Watch the Release Video](https://docs.crawl4ai.com/blog/releases/0.6.0/#watch-the-release-video)
  * [Join the Community](https://docs.crawl4ai.com/blog/releases/0.6.0/#join-the-community)
  * [Install or Upgrade](https://docs.crawl4ai.com/blog/releases/0.6.0/#install-or-upgrade)


* * *
> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")
