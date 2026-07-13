from __future__ import annotations

import html
import json
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "source" / "puzzles.json"
PUZZLE_DIR = ROOT / "puzzles"
SITE_URL = "https://micavro.github.io/puzzlecat-mon7tr"


def render_markdown(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "sane_lists"],
        output_format="html5",
    )


def page_head(title: str, description: str, asset_prefix: str = "") -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <meta name="theme-color" content="#f5f1e8">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{asset_prefix}assets/styles.css">
</head>
"""


def topbar(prefix: str = "") -> str:
    return f"""<header class="topbar">
  <a class="brand" href="{prefix}index.html"><span class="cat-mark">PC</span><span>PuzzleCat Solve Logs</span></a>
  <div class="top-actions">
    <a class="github-link" href="https://github.com/micavro/puzzlecat-mon7tr" target="_blank" rel="noreferrer">GitHub</a>
    <button class="icon-button" id="themeButton" aria-label="切换深浅色">◐</button>
  </div>
</header>"""


def load_puzzles() -> list[dict[str, str | int]]:
    puzzles = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if len(puzzles) != 289:
        raise RuntimeError(f"Expected 289 puzzles, found {len(puzzles)}")
    for puzzle in puzzles:
        log_path = ROOT / "source" / str(puzzle["log_file"])
        puzzle["log_text"] = log_path.read_text(encoding="utf-8")
        puzzle["log_html"] = render_markdown(str(puzzle["log_text"]))
    return puzzles


def build_index(puzzles: list[dict[str, str | int]]) -> str:
    cards = []
    for puzzle in puzzles:
        number = int(puzzle["number"])
        puzzle_id = str(puzzle["id"])
        title = str(puzzle["title"])
        slug = str(puzzle["slug"])
        search_text = f"{title} {puzzle_id}".casefold()
        line_count = len(str(puzzle["log_text"]).splitlines())
        cards.append(
            f'<article class="puzzle-card log-card" data-search="{html.escape(search_text, quote=True)}">'
            f'<a href="puzzles/{slug}.html">'
            f'<div class="card-top"><span class="card-number">{number:03d}</span><code>{puzzle_id}</code></div>'
            f'<h2>{html.escape(title)}</h2>'
            f'<div class="log-card-meta"><span>solve-log.md</span><strong>{line_count} 行</strong></div>'
            f'<div class="card-footer">查看原始解题日志 <span>→</span></div>'
            f'</a></article>'
        )

    return f"""{page_head('PuzzleCat Solve Logs', 'PuzzleCat 289 道已正确题目的原始 solve-log.md 可视化索引。')}
<body class="index-page">
  {topbar()}
  <main id="top" class="index-main">
    <section class="hero compact-hero">
      <div class="hero-kicker">PUZZLECAT · ORIGINAL SOLVE LOGS</div>
      <h1>289 份解题日志</h1>
      <p class="hero-lead">每个页面只展示对应的原始 <code>solve-log.md</code>，正文不改写、不摘要、不补充。</p>
      <div class="stats">
        <div><strong>289</strong><span>独立日志页面</span></div>
        <div><strong>1:1</strong><span>原文件复制</span></div>
        <div><strong>SHA</strong><span>内容一致性校验</span></div>
      </div>
      <div class="main-search">
        <label for="searchInput">搜索题目或 Puzzle ID</label>
        <input id="searchInput" type="search" placeholder="例如：Cryptic / 月照纱窗 / 题目 ID" autocomplete="off">
        <span><strong id="resultCount">289</strong> / 289 份</span>
      </div>
    </section>
    <section class="log-notice"><strong>展示原则</strong><span>HTML 仅负责 Markdown 排版和页面导航；日志文字来自本地 solve-log.md 原文件。</span></section>
    <div id="noResults" class="no-results" hidden><strong>没有匹配的日志</strong><span>换一个题名或 Puzzle ID 试试。</span></div>
    <section class="puzzle-grid" id="puzzleGrid">{''.join(cards)}</section>
    <footer><p>PuzzleCat Solve Logs · 289 个原始日志页面</p><a href="#top">返回顶部 ↑</a></footer>
  </main>
  <script src="assets/app.js"></script>
</body>
</html>
"""


def build_puzzle_page(
    puzzle: dict[str, str | int],
    previous: dict[str, str | int] | None,
    following: dict[str, str | int] | None,
) -> str:
    number = int(puzzle["number"])
    puzzle_id = str(puzzle["id"])
    title = str(puzzle["title"])
    slug = str(puzzle["slug"])
    original_url = str(puzzle["original_url"])

    previous_link = (
        f'<a class="sequence-link previous" href="{previous["slug"]}.html"><span>← 上一份日志</span><strong>{html.escape(str(previous["title"]))}</strong></a>'
        if previous
        else '<span class="sequence-link disabled"></span>'
    )
    following_link = (
        f'<a class="sequence-link next" href="{following["slug"]}.html"><span>下一份日志 →</span><strong>{html.escape(str(following["title"]))}</strong></a>'
        if following
        else '<span class="sequence-link disabled"></span>'
    )

    return f"""{page_head(f'{title} · Solve Log', f'{title}（{puzzle_id}）的原始 solve-log.md。', '../')}
<body class="detail-page" id="top">
  {topbar('../')}
  <main class="detail-main log-detail-main">
    <nav class="breadcrumb"><a href="../index.html">全部日志</a><span>/</span><span>{number:03d}</span></nav>
    <header class="log-page-header">
      <div><span class="log-sequence">{number:03d} / 289</span><code>{puzzle_id}</code></div>
      <h1>{html.escape(title)}</h1>
      <div class="log-toolbar">
        <a href="{html.escape(original_url, quote=True)}" target="_blank" rel="noreferrer">打开 PuzzleCat 原题 ↗</a>
        <a href="../source/solve-logs/{slug}.md">查看原始 Markdown</a>
      </div>
    </header>
    <article class="solve-log-document">{puzzle['log_html']}</article>
    <nav class="sequence-nav">{previous_link}{following_link}</nav>
    <div class="back-index"><a href="../index.html">返回全部 289 份日志</a></div>
    <footer><p>{html.escape(title)} · solve-log.md</p><a href="#top">返回顶部 ↑</a></footer>
  </main>
  <script src="../assets/app.js"></script>
</body>
</html>
"""


def build_sitemap(puzzles: list[dict[str, str | int]]) -> str:
    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/puzzles/{p['slug']}.html" for p in puzzles]
    entries = "".join(f"<url><loc>{html.escape(url)}</loc></url>" for url in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{entries}</urlset>'


def main() -> None:
    puzzles = load_puzzles()
    ROOT.joinpath("index.html").write_text(build_index(puzzles), encoding="utf-8")
    PUZZLE_DIR.mkdir(exist_ok=True)
    for old_page in PUZZLE_DIR.glob("*.html"):
        old_page.unlink()
    for index, puzzle in enumerate(puzzles):
        previous = puzzles[index - 1] if index else None
        following = puzzles[index + 1] if index + 1 < len(puzzles) else None
        PUZZLE_DIR.joinpath(f"{puzzle['slug']}.html").write_text(
            build_puzzle_page(puzzle, previous, following),
            encoding="utf-8",
        )
    ROOT.joinpath("sitemap.xml").write_text(build_sitemap(puzzles), encoding="utf-8")
    print(f"Built index and {len(puzzles)} unmodified solve-log pages")


if __name__ == "__main__":
    main()
