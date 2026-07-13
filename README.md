# puzzlecat-mon7tr

PuzzleCat 289 份原始 `solve-log.md` 的静态可视化网站。

在线访问：<https://micavro.github.io/puzzlecat-mon7tr/>

## 展示原则

- 每个题目页面只渲染对应的原始 `solve-log.md`；
- 不改写、摘要或补充日志正文；
- HTML 只提供 Markdown 排版、搜索、原题链接和前后导航；
- `source/solve-logs/` 中的日志副本与工作区原文件经过 SHA-256 一致性校验。

## 本地构建

```powershell
python -m pip install -r requirements.txt
python build_site.py
python -m http.server 8000
```

生成内容：

- `index.html`：289 份日志的搜索索引；
- `puzzles/*.html`：格式化后的独立日志页面；
- `source/solve-logs/*.md`：未经修改的原始日志副本；
- `source/puzzles.json`：页面标题、ID、文件名和原题 URL 映射；
- `sitemap.xml`：GitHub Pages 页面索引。
