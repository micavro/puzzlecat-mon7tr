# puzzlecat-mon7tr

PuzzleCat 289 道独立题解的静态网页版本。主页提供搜索索引，`puzzles/` 中每道题拥有独立 HTML 页面与稳定 URL。

在线访问：<https://micavro.github.io/puzzlecat-mon7tr/>

## 本地构建

```powershell
python -m pip install -r requirements.txt
python build_site.py
python -m http.server 8000
```

然后访问 <http://localhost:8000/>。

题解来源位于 `source/PuzzleCat-Solutions.md`，本地提交统计位于 `source/puzzle-metadata.json`。运行构建脚本后会生成：

- `index.html`：主页与 289 题搜索索引；
- `puzzles/*.html`：289 个独立题解页面；
- `sitemap.xml`：GitHub Pages 页面索引；
- `assets/`：共享样式与交互脚本。
