<!-- Source: https://docs.crawl4ai.com/apps/llmtxt/build/ -->

[Crawl4AI Documentation (v0.7.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Code Examples ](https://docs.crawl4ai.com/core/examples/)
  * [ Search ](https://docs.crawl4ai.com/apps/llmtxt/build/)


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


O**Prompt for AI Coding Assistant: Create an Interactive LLM Context Builder Page**
**Objective:**
Your task is to create an interactive HTML webpage with JavaScript functionality that allows users to select and combine different `crawl4ai` LLM context files into a single downloadable Markdown (`.md`) file. This tool will empower users to craft tailored context for their AI assistants based on their specific needs.
**Core Functionality:**
  1. **Display`crawl4ai` Components:** The page will list all available `crawl4ai` documentation components.
  2. **Select Context Types:** For each component, users can select which types of context they want to include:
     * Memory (API facts)
     * Reasoning (How-to/why)
     * Examples (Code snippets) (All should be selected by default for each initially selected component).
  3. **Special "Aggregate" Contexts:** Include options for special, pre-combined contexts:
     * "Vibe Coding" (a curated mix for general AI prompting)
     * "All Library Context" (a comprehensive aggregation of all memory, reasoning, and examples for the entire library).
  4. **Fetch and Concatenate:** When the user clicks a "Download Combined Context" button:
     * The JavaScript will fetch the content of all selected Markdown files from the server (from a predefined folder, e.g., `/llmtxt/`).
     * It will concatenate the content of these files into a single string.
  5. **Client-Side Download:** The concatenated content will be offered to the user as a download (e.g., `custom_crawl4ai_context.md`).


**Input/Assumptions:**
  * **Context Files Location:** All individual context Markdown files are located on the server in a publicly accessible folder named `llmtxt/`.
  * **File Naming Convention:** Files follow the pattern: `crawl4ai_{{component_name}}_[memory|reasoning|examples]_content.llm.md`.
    * `{{component_name}}` can contain underscores (e.g., `deep_crawling`, `config_objects`).
    * The special contexts will have names like `crawl4ai_vibe_content.llm.md` and `crawl4ai_all_content.llm.md`.
  * **Component List:** You will be provided with a list of `crawl4ai` components. For this implementation, use the following list:
    * `core`
    * `config_objects`
    * `deep_crawling`
    * `deployment` (covers Installation & Docker Deployment)
    * `extraction` (covers Structured Data Extraction)
    * `markdown` (covers Markdown Generation Algorithm)
    * `pdf_processing`
    * _(No separate "Vibe Coding" or "All Library Context" in this list, as they are special top-level selections)_


**Detailed UI/UX Requirements:**
  1. **Main Page Structure:**
     * **Header:** "Crawl4AI Interactive LLM Context Builder"
     * **Introduction:** Briefly explain the purpose of the tool (from the `USING_LLM_CONTEXTS.md` content you helped draft: "Supercharging Your AI Assistant...").
     * **Selection Area:**
       * **Special Aggregate Contexts (Radio Buttons or Prominent Checkboxes):**
         * [ ] "Vibe Coding Context" (`crawl4ai_vibe_content.llm.md`)
         * [ ] "All Library Context (Comprehensive)" (`crawl4ai_all_content.llm.md`)
         * _Behavior:_ Selecting one of these might disable individual component selections (or vice-versa) to avoid redundancy, or simply add them to the list. Consider user experience here. A simple approach is that if an aggregate is selected, it's the _only_ thing downloaded.
       * **Individual Component Selection (Table or List of Checkboxes):**
         * A section titled "Select Individual Components & Context Types:"
         * For each component in the provided list:
           * A master checkbox for the component itself (e.g., `[ ] Core Functionality`). Selected by default.
           * Nested checkboxes (indented or grouped) for context types, enabled only if the parent component is checked:
             * `[x] Memory (API Facts)`
             * `[x] Reasoning (How-to/Why)`
             * `[x] Examples (Code Snippets)` (These three sub-checkboxes should be selected by default if the parent component is selected).
     * **Action Button:**
       * A button: "Generate & Download Combined Context"
     * **Status/Feedback Area:** (Optional, but good UX)
       * Display messages like "Fetching files...", "Combining context...", "Download starting..." or error messages.


**Final Output:**
  * A single HTML file (e.g., `interactive_context_builder.html`).
  * Associated JavaScript code (can be inline within `<script>` tags or in a separate `.js` file).
  * Associated CSS code (can be inline within `<style>` tags or in a separate `.css` file).


This interactive tool will greatly enhance the user experience for `crawl4ai` developers looking to leverage your specialized LLM contexts. Please ensure the JavaScript is robust and provides good user feedback.
* * *
This prompt should give your AI coding assistant a very clear set of requirements and guidelines for building the interactive context builder. Remember to provide it with the list of components as mentioned in the "Input/Assumptions" section.
* * *
> Feedback 
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")
