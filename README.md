# sitecrawl

基于 crawl4ai 的轻量级站点爬虫，用于从网站地图批量生成 Markdown 内容。

## 功能说明

- `crawl.py`：使用 crawl4ai 的 URL 播种能力，自动发现目标域名的所有页面，生成合并去重的 `sitemap.xml`，并输出简单的页面分类统计。
- `crawlRoute.py`：只使用 BFS 策略，不做 sitemap 播种；当目标包含路径时，仅抓取该路径及其子路径的页面。
- `md.py`：解析现有的 `sitemap.xml`，逐个调用 crawl4ai 获取页面 Markdown，按 URL 生成唯一文件名并写入 `mdoutput/` 文件夹。

## 使用方法

### 全站爬取

1. 打开 `crawl.py`，把 `DOMAIN` 改成需要分析的域名（只填域名，无协议前缀）。
2. 运行 `uv run crawl.py`：脚本会自动抓取目标站点并生成/更新 `sitemap.xml`。

### 指定路径爬取

1. 打开 `crawlRoute.py`，把 `TARGET` 改成目标（可以带路径，例如 `ant-design.antgroup.com/components`）。
2. 运行 `uv run crawlRoute.py`：脚本会从指定路径出发，使用广度优先在同一域名下最多爬取 5 层深度，并生成 `sitemap.xml`。

> 无论使用哪种方式，都可以事后直接编辑 `sitemap.xml` 中的 `<loc>` 条目，然后继续下一步。

### Markdown 输出

运行 `uv run md.py`：程序会根据 `sitemap.xml` 爬取所有 URL，并在 `mdoutput/` 下生成对应的 Markdown 文件。

- 如果想一键完成「全站爬取 + Markdown 导出」，可以在确认无重要旧输出后执行 `rm -rf mdoutput/ sitemap.xml && uv run crawl.py && uv run md.py`。

## 输出结果

- 站点地图：`./sitemap.xml`
- Markdown 文件：`./mdoutput/*.md`（文件名会根据 URL 自动生成并去重）。

## 环境需求

- Python 3.13 及以上
- `uv`（用于安装和运行 crawl4ai）
