<!-- Source: https://docs.crawl4ai.com/blog/releases/0.7.2/ -->

[Crawl4AI Documentation (v0.7.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/0.7.2/)


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
  * [🚀 Crawl4AI v0.7.2: CI/CD & Dependency Optimization Update](https://docs.crawl4ai.com/blog/releases/0.7.2/#crawl4ai-v072-cicd-dependency-optimization-update)
  * [🎯 What's New](https://docs.crawl4ai.com/blog/releases/0.7.2/#whats-new)
  * [🏗️ CI/CD Pipeline](https://docs.crawl4ai.com/blog/releases/0.7.2/#cicd-pipeline)
  * [💾 Lighter Installation](https://docs.crawl4ai.com/blog/releases/0.7.2/#lighter-installation)
  * [🐳 Docker Improvements](https://docs.crawl4ai.com/blog/releases/0.7.2/#docker-improvements)
  * [🔧 Technical Details](https://docs.crawl4ai.com/blog/releases/0.7.2/#technical-details)
  * [🚀 Installation](https://docs.crawl4ai.com/blog/releases/0.7.2/#installation)


# 🚀 Crawl4AI v0.7.2: CI/CD & Dependency Optimization Update
_July 25, 2025 • 3 min read_
* * *
This release introduces automated CI/CD pipelines for seamless releases and optimizes dependencies for a lighter, more efficient package.
## 🎯 What's New
### 🔄 Automated Release Pipeline
  * **GitHub Actions CI/CD** : Automated PyPI and Docker Hub releases on tag push
  * **Multi-platform Docker images** : Support for both AMD64 and ARM64 architectures
  * **Version consistency checks** : Ensures tag, package, and Docker versions align
  * **Automated release notes** : GitHub releases created automatically


### 📦 Dependency Optimization
  * **Moved sentence-transformers to optional dependencies** : Significantly reduces default installation size
  * **Lighter Docker images** : Optimized Dockerfile for faster builds and smaller images
  * **Better dependency management** : Core vs. optional dependencies clearly separated


## 🏗️ CI/CD Pipeline
The new automated release process ensures consistent, reliable releases:
```
# Trigger releases with a simple tag
git tag v0.7.2
git push origin v0.7.2

# Automatically:
# ✅ Validates version consistency
# ✅ Builds and publishes to PyPI
# ✅ Builds multi-platform Docker images
# ✅ Pushes to Docker Hub with proper tags
# ✅ Creates GitHub release
Copy
```

## 💾 Lighter Installation
Default installation is now significantly smaller:
```
# Core installation (smaller, faster)
pip install crawl4ai==0.7.2

# With ML features (includes sentence-transformers)
pip install crawl4ai[transformer]==0.7.2

# Full installation
pip install crawl4ai[all]==0.7.2
Copy
```

## 🐳 Docker Improvements
Enhanced Docker support with multi-platform images:
```
# Pull the latest version
docker pull unclecode/crawl4ai:0.7.2
docker pull unclecode/crawl4ai:latest

# Available tags:
# - unclecode/crawl4ai:0.7.2 (specific version)
# - unclecode/crawl4ai:0.7 (minor version)
# - unclecode/crawl4ai:0 (major version)
# - unclecode/crawl4ai:latest
Copy
```

## 🔧 Technical Details
### Dependency Changes
  * `sentence-transformers` moved from required to optional dependencies
  * Reduces default installation by ~500MB
  * No impact on functionality when transformer features aren't needed


### CI/CD Configuration
  * GitHub Actions workflows for automated releases
  * Version validation before publishing
  * Parallel PyPI and Docker Hub deployments
  * Automatic tagging strategy for Docker images


## 🚀 Installation
```
pip install crawl4ai==0.7.2
Copy
```

No breaking changes - direct upgrade from v0.7.0 or v0.7.1.
* * *
Questions? Issues? - GitHub: [github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) - Discord: [discord.gg/crawl4ai](https://discord.gg/jP8KfhDhyN) - Twitter: [@unclecode](https://x.com/unclecode)
_P.S. The new CI/CD pipeline will make future releases faster and more reliable. Thanks for your patience as we improve our release process!_
#### On this page
  * [🎯 What's New](https://docs.crawl4ai.com/blog/releases/0.7.2/#whats-new)
  * [🔄 Automated Release Pipeline](https://docs.crawl4ai.com/blog/releases/0.7.2/#automated-release-pipeline)
  * [📦 Dependency Optimization](https://docs.crawl4ai.com/blog/releases/0.7.2/#dependency-optimization)
  * [🏗️ CI/CD Pipeline](https://docs.crawl4ai.com/blog/releases/0.7.2/#cicd-pipeline)
  * [💾 Lighter Installation](https://docs.crawl4ai.com/blog/releases/0.7.2/#lighter-installation)
  * [🐳 Docker Improvements](https://docs.crawl4ai.com/blog/releases/0.7.2/#docker-improvements)
  * [🔧 Technical Details](https://docs.crawl4ai.com/blog/releases/0.7.2/#technical-details)
  * [Dependency Changes](https://docs.crawl4ai.com/blog/releases/0.7.2/#dependency-changes)
  * [CI/CD Configuration](https://docs.crawl4ai.com/blog/releases/0.7.2/#cicd-configuration)
  * [🚀 Installation](https://docs.crawl4ai.com/blog/releases/0.7.2/#installation)


* * *
> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")
