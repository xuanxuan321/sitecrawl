<!-- Source: https://docs.crawl4ai.com/basic/installation/ -->

[Crawl4AI Documentation (v0.7.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/basic/installation/)


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
  * [Installation 💻](https://docs.crawl4ai.com/basic/installation/#installation)
  * [Option 1: Python Package Installation (Recommended)](https://docs.crawl4ai.com/basic/installation/#option-1-python-package-installation-recommended)
  * [Playwright Installation Note for Ubuntu](https://docs.crawl4ai.com/basic/installation/#playwright-installation-note-for-ubuntu)
  * [Option 2: Using Docker (Coming Soon)](https://docs.crawl4ai.com/basic/installation/#option-2-using-docker-coming-soon)
  * [Option 3: Local Server Installation](https://docs.crawl4ai.com/basic/installation/#option-3-local-server-installation)
  * [Verifying Your Installation](https://docs.crawl4ai.com/basic/installation/#verifying-your-installation)
  * [Getting Help](https://docs.crawl4ai.com/basic/installation/#getting-help)


# Installation 💻
Crawl4AI offers flexible installation options to suit various use cases. You can install it as a Python package, use it with Docker, or run it as a local server.
## Option 1: Python Package Installation (Recommended)
Crawl4AI is now available on PyPI, making installation easier than ever. Choose the option that best fits your needs:
### Basic Installation
For basic web crawling and scraping tasks:
```
pip install crawl4ai
playwright install # Install Playwright dependencies
Copy
```

### Installation with PyTorch
For advanced text clustering (includes CosineSimilarity cluster strategy):
```
pip install crawl4ai[torch]
Copy
```

### Installation with Transformers
For text summarization and Hugging Face models:
```
pip install crawl4ai[transformer]
Copy
```

### Full Installation
For all features:
```
pip install crawl4ai[all]
Copy
```

### Development Installation
For contributors who plan to modify the source code:
```
git clone https://github.com/unclecode/crawl4ai.git
cd crawl4ai
pip install -e ".[all]"
playwright install # Install Playwright dependencies
Copy
```

💡 After installation with "torch", "transformer", or "all" options, it's recommended to run the following CLI command to load the required models:
```
crawl4ai-download-models
Copy
```

This is optional but will boost the performance and speed of the crawler. You only need to do this once after installation.
## Playwright Installation Note for Ubuntu
If you encounter issues with Playwright installation on Ubuntu, you may need to install additional dependencies:
```
sudo apt-get install -y \
    libwoff1 \
    libopus0 \
    libwebp7 \
    libwebpdemux2 \
    libenchant-2-2 \
    libgudev-1.0-0 \
    libsecret-1-0 \
    libhyphen0 \
    libgdk-pixbuf2.0-0 \
    libegl1 \
    libnotify4 \
    libxslt1.1 \
    libevent-2.1-7 \
    libgles2 \
    libxcomposite1 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libepoxy0 \
    libgtk-3-0 \
    libharfbuzz-icu0 \
    libgstreamer-gl1.0-0 \
    libgstreamer-plugins-bad1.0-0 \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    libxt6 \
    libxaw7 \
    xvfb \
    fonts-noto-color-emoji \
    libfontconfig \
    libfreetype6 \
    xfonts-cyrillic \
    xfonts-scalable \
    fonts-liberation \
    fonts-ipafont-gothic \
    fonts-wqy-zenhei \
    fonts-tlwg-loma-otf \
    fonts-freefont-ttf
Copy
```

## Option 2: Using Docker (Coming Soon)
Docker support for Crawl4AI is currently in progress and will be available soon. This will allow you to run Crawl4AI in a containerized environment, ensuring consistency across different systems.
## Option 3: Local Server Installation
For those who prefer to run Crawl4AI as a local server, instructions will be provided once the Docker implementation is complete.
## Verifying Your Installation
After installation, you can verify that Crawl4AI is working correctly by running a simple Python script:
```
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.example.com")
        print(result.markdown[:500])  # Print first 500 characters

if __name__ == "__main__":
    asyncio.run(main())
Copy
```

This script should successfully crawl the example website and print the first 500 characters of the extracted content.
## Getting Help
If you encounter any issues during installation or usage, please check the [documentation](https://docs.crawl4ai.com/) or raise an issue on the [GitHub repository](https://github.com/unclecode/crawl4ai/issues).
Happy crawling! 🕷️🤖
#### On this page
  * [Option 1: Python Package Installation (Recommended)](https://docs.crawl4ai.com/basic/installation/#option-1-python-package-installation-recommended)
  * [Basic Installation](https://docs.crawl4ai.com/basic/installation/#basic-installation)
  * [Installation with PyTorch](https://docs.crawl4ai.com/basic/installation/#installation-with-pytorch)
  * [Installation with Transformers](https://docs.crawl4ai.com/basic/installation/#installation-with-transformers)
  * [Full Installation](https://docs.crawl4ai.com/basic/installation/#full-installation)
  * [Development Installation](https://docs.crawl4ai.com/basic/installation/#development-installation)
  * [Playwright Installation Note for Ubuntu](https://docs.crawl4ai.com/basic/installation/#playwright-installation-note-for-ubuntu)
  * [Option 2: Using Docker (Coming Soon)](https://docs.crawl4ai.com/basic/installation/#option-2-using-docker-coming-soon)
  * [Option 3: Local Server Installation](https://docs.crawl4ai.com/basic/installation/#option-3-local-server-installation)
  * [Verifying Your Installation](https://docs.crawl4ai.com/basic/installation/#verifying-your-installation)
  * [Getting Help](https://docs.crawl4ai.com/basic/installation/#getting-help)


* * *
> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")
