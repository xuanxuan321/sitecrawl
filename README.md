# sitecrawl

基于 crawl4ai 的轻量级站点爬虫，用于从网站地图批量生成 Markdown 内容。

## 功能说明

- `crawl.py`：使用 crawl4ai 的 URL 播种能力，自动发现目标域名的所有页面，生成合并去重的 `sitemap.xml`，并输出简单的页面分类统计。
- `md.py`：解析现有的 `sitemap.xml`，逐个调用 crawl4ai 获取页面 Markdown，按 URL 生成唯一文件名并写入 `mdoutput/` 文件夹。

## 使用方法

1. 打开 `crawl.py`，把 `DOMAIN` 改成需要分析的域名（只填域名，无协议前缀）。
2. 运行 `uv run crawl.py`：脚本会自动抓取目标站点并生成/更新 `sitemap.xml`。
3. 如需修改站点列表，可直接编辑 `sitemap.xml` 中的 `<loc>` 条目。
4. 运行 `uv run md.py`：程序会根据站点地图爬取所有 URL，并在 `mdoutput/` 下生成对应的 Markdown 文件。
5. 若想直接从域名生成 markdown，只需运行 `uv run crawl.py&&uv run md.py` 即可。

## 输出结果

- 站点地图：`./sitemap.xml`
- Markdown 文件：`./mdoutput/*.md`（文件名会根据 URL 自动生成并去重）。

## 环境需求

- Python 3.13 及以上
- `uv`（用于安装和运行 crawl4ai）
