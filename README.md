# puzzlecat-mon7tr

PuzzleCat 289 道独立题解的静态网页版本。

在线访问：<https://micavro.github.io/puzzlecat-mon7tr/>

## 本地构建

```powershell
python -m pip install -r requirements.txt
python build_site.py
python -m http.server 8000
```

然后访问 <http://localhost:8000/>。

题解来源位于 `source/PuzzleCat-Solutions.md`。生成后的 `index.html`、`assets/styles.css` 和 `assets/app.js` 可直接由 GitHub Pages 托管。
