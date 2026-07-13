from __future__ import annotations

import html
import json
import re
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source" / "PuzzleCat-Solutions.md"
OUTPUT = ROOT / "index.html"


def render_markdown(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "sane_lists"],
        output_format="html5",
    )


def parse_source(text: str) -> tuple[str, list[dict[str, str]]]:
    intro = text.split("## 题目索引", 1)[0].strip()
    solution_text = text.split("## 逐题题解", 1)[1]
    starts = list(
        re.finditer(
            r'<a id="p-([A-Za-z0-9]{8})"></a>\s*\n\s*## ([^\n]+)',
            solution_text,
        )
    )

    puzzles: list[dict[str, str]] = []
    for index, match in enumerate(starts):
        puzzle_id = match.group(1)
        heading = match.group(2).strip()
        end = starts[index + 1].start() if index + 1 < len(starts) else len(solution_text)
        chunk = solution_text[match.end() : end].strip()
        answer_match = re.search(r"^- 答案：`([^`]+)`", chunk, re.MULTILINE)
        answer = answer_match.group(1) if answer_match else ""
        title = re.sub(rf"（{re.escape(puzzle_id)}）$", "", heading).strip()
        puzzles.append(
            {
                "id": puzzle_id,
                "title": title,
                "answer": answer,
                "html": render_markdown(chunk),
            }
        )

    if len(puzzles) != 289:
        raise RuntimeError(f"Expected 289 puzzles, found {len(puzzles)}")
    return render_markdown(intro), puzzles


def build_page(intro_html: str, puzzles: list[dict[str, str]]) -> str:
    nav_items = []
    sections = []
    for number, puzzle in enumerate(puzzles, 1):
        puzzle_id = puzzle["id"]
        title = puzzle["title"]
        answer = puzzle["answer"]
        search_text = " ".join((title, puzzle_id, answer)).casefold()
        nav_items.append(
            f'<li data-search="{html.escape(search_text, quote=True)}">'
            f'<a href="#p-{puzzle_id}"><span class="nav-number">{number:03d}</span>'
            f'<span class="nav-title">{html.escape(title)}</span></a></li>'
        )
        sections.append(
            f'<section class="puzzle" id="p-{puzzle_id}" '
            f'data-search="{html.escape(search_text, quote=True)}">'
            f'<header class="puzzle-heading"><span class="puzzle-number">{number:03d}</span>'
            f'<div><h2>{html.escape(title)}</h2><code>{puzzle_id}</code></div>'
            f'<a class="permalink" href="#p-{puzzle_id}" aria-label="复制本题链接">#</a></header>'
            f'<div class="puzzle-content">{puzzle["html"]}</div></section>'
        )

    metadata = json.dumps(
        {"count": len(puzzles), "generatedFrom": SOURCE.name},
        ensure_ascii=False,
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="PuzzleCat 289 道独立题解全集，基于本地解题日志整理。">
  <meta name="theme-color" content="#f5f1e8">
  <title>PuzzleCat 独立题解全集</title>
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  <header class="topbar">
    <button class="icon-button menu-button" id="menuButton" aria-label="打开题目目录">☰</button>
    <a class="brand" href="#top"><span class="cat-mark">PC</span><span>PuzzleCat 独立题解</span></a>
    <div class="top-actions">
      <a class="github-link" href="https://github.com/micavro/puzzlecat-mon7tr" target="_blank" rel="noreferrer">GitHub</a>
      <button class="icon-button" id="themeButton" aria-label="切换深浅色">◐</button>
    </div>
  </header>

  <aside class="sidebar" id="sidebar" aria-label="题目目录">
    <div class="search-wrap">
      <label for="searchInput">搜索题目、ID 或答案</label>
      <input id="searchInput" type="search" placeholder="例如：Cryptic / SWIFT / 题目 ID" autocomplete="off">
      <div class="search-meta"><span id="resultCount">289</span> / 289 道</div>
    </div>
    <nav><ol id="puzzleNav">{''.join(nav_items)}</ol></nav>
  </aside>
  <div class="sidebar-backdrop" id="sidebarBackdrop"></div>

  <main id="top">
    <section class="hero">
      <div class="hero-kicker">PUZZLECAT · SOLUTION ARCHIVE</div>
      <h1>独立题解全集</h1>
      <p class="hero-lead">289 道已正确题目的本地独立解法。没有用官方题解补写机制；证据不足的地方保留原始边界。</p>
      <div class="stats">
        <div><strong>289</strong><span>已完成题目</span></div>
        <div><strong>4</strong><span>整理批次</span></div>
        <div><strong>26</strong><span>证据边界标记</span></div>
      </div>
      <a class="start-button" href="#p-{puzzles[0]['id']}">开始阅读 <span>↓</span></a>
    </section>

    <section class="method-note">
      <div class="note-icon">i</div>
      <div>{intro_html}</div>
    </section>

    <div id="noResults" class="no-results" hidden>
      <strong>没有匹配的题目</strong>
      <span>换一个标题、ID 或答案试试。</span>
    </div>

    <article id="solutions">{''.join(sections)}</article>
    <footer>
      <p>PuzzleCat 独立题解全集 · 由本地解题归档生成</p>
      <a href="#top">返回顶部 ↑</a>
    </footer>
  </main>

  <script type="application/json" id="siteMetadata">{html.escape(metadata)}</script>
  <script src="assets/app.js"></script>
</body>
</html>
"""


def main() -> None:
    intro_html, puzzles = parse_source(SOURCE.read_text(encoding="utf-8"))
    OUTPUT.write_text(build_page(intro_html, puzzles), encoding="utf-8")
    print(f"Built {OUTPUT} with {len(puzzles)} puzzles")


if __name__ == "__main__":
    main()
