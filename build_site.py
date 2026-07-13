from __future__ import annotations

import html
import json
import re
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source" / "PuzzleCat-Solutions.md"
METADATA = ROOT / "source" / "puzzle-metadata.json"
PUZZLE_LINKS = ROOT / "source" / "puzzle-links.json"
PUZZLE_DIR = ROOT / "puzzles"
SITE_URL = "https://micavro.github.io/puzzlecat-mon7tr"


def render_markdown(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "sane_lists"],
        output_format="html5",
    )


def parse_source(
    text: str,
    metadata: dict[str, dict],
    puzzle_links: dict[str, str],
) -> tuple[str, list[dict[str, str | int]]]:
    intro = text.split("## 题目索引", 1)[0].strip()
    solution_text = text.split("## 逐题题解", 1)[1]
    starts = list(
        re.finditer(
            r'<a id="p-([A-Za-z0-9]{8})"></a>\s*\n\s*## ([^\n]+)',
            solution_text,
        )
    )

    puzzles: list[dict[str, str | int]] = []
    for index, match in enumerate(starts):
        puzzle_id = match.group(1)
        heading = match.group(2).strip()
        end = starts[index + 1].start() if index + 1 < len(starts) else len(solution_text)
        chunk = solution_text[match.end() : end].strip()
        answer_match = re.search(r"^- 答案：`([^`]+)`", chunk, re.MULTILINE)
        answer = answer_match.group(1) if answer_match else ""
        content = re.sub(r"^- 答案：`[^`]+`\s*", "", chunk, count=1, flags=re.MULTILINE).strip()
        title = re.sub(rf"（{re.escape(puzzle_id)}）$", "", heading).strip()
        outcome = metadata.get(puzzle_id, {})
        puzzles.append(
            {
                "id": puzzle_id,
                "title": title,
                "answer": answer,
                "html": render_markdown(content),
                "incorrect": int(outcome.get("incorrect", 0)),
                "original_url": puzzle_links.get(puzzle_id, f"https://puzzle.cat/puzzles/{puzzle_id}"),
            }
        )

    if len(puzzles) != 289:
        raise RuntimeError(f"Expected 289 puzzles, found {len(puzzles)}")
    return render_markdown(intro), puzzles


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
  <a class="brand" href="{prefix}index.html"><span class="cat-mark">PC</span><span>PuzzleCat 独立题解</span></a>
  <div class="top-actions">
    <a class="github-link" href="https://github.com/micavro/puzzlecat-mon7tr" target="_blank" rel="noreferrer">GitHub</a>
    <button class="icon-button" id="themeButton" aria-label="切换深浅色">◐</button>
  </div>
</header>"""


def build_index(intro_html: str, puzzles: list[dict[str, str | int]]) -> str:
    cards = []
    for number, puzzle in enumerate(puzzles, 1):
        puzzle_id = str(puzzle["id"])
        title = str(puzzle["title"])
        answer = str(puzzle["answer"])
        search_text = " ".join((title, puzzle_id, answer)).casefold()
        cards.append(
            f'<article class="puzzle-card" data-search="{html.escape(search_text, quote=True)}">'
            f'<a href="puzzles/{puzzle["slug"]}.html">'
            f'<div class="card-top"><span class="card-number">{number:03d}</span><code>{puzzle_id}</code></div>'
            f'<h2>{html.escape(title)}</h2>'
            f'<div class="card-answer"><span>答案</span><strong>{html.escape(answer)}</strong></div>'
            f'<div class="card-footer">阅读完整题解 <span>→</span></div>'
            f'</a></article>'
        )

    return f"""{page_head('PuzzleCat 独立题解全集', 'PuzzleCat 289 道独立题解全集，每题拥有独立页面。')}
<body class="index-page">
  {topbar()}
  <main id="top" class="index-main">
    <section class="hero compact-hero">
      <div class="hero-kicker">PUZZLECAT · 289 INDIVIDUAL SOLUTIONS</div>
      <h1>独立题解全集</h1>
      <p class="hero-lead">每道题都拥有独立 HTML 页面、稳定链接和前后导航。主页负责搜索，题目页负责完整呈现解题过程。</p>
      <div class="stats">
        <div><strong>289</strong><span>独立题目页面</span></div>
        <div><strong>289</strong><span>已正确答案</span></div>
        <div><strong>26</strong><span>证据边界标记</span></div>
      </div>
      <div class="main-search">
        <label for="searchInput">搜索题目、ID 或答案</label>
        <input id="searchInput" type="search" placeholder="例如：Cryptic / SWIFT / 题目 ID" autocomplete="off">
        <span><strong id="resultCount">289</strong> / 289 道</span>
      </div>
    </section>

    <section class="method-note index-note">
      <div class="note-icon">i</div>
      <div>{intro_html}</div>
    </section>

    <div id="noResults" class="no-results" hidden>
      <strong>没有匹配的题目</strong><span>换一个标题、ID 或答案试试。</span>
    </div>
    <section class="puzzle-grid" id="puzzleGrid">{''.join(cards)}</section>
    <footer><p>PuzzleCat 独立题解全集 · 289 个独立 HTML 页面</p><a href="#top">返回顶部 ↑</a></footer>
  </main>
  <script src="assets/app.js"></script>
</body>
</html>
"""


def build_puzzle_page(
    puzzle: dict[str, str | int],
    number: int,
    previous: dict[str, str | int] | None,
    following: dict[str, str | int] | None,
) -> str:
    puzzle_id = str(puzzle["id"])
    title = str(puzzle["title"])
    answer = str(puzzle["answer"])
    incorrect = int(puzzle["incorrect"])
    original_url = str(puzzle["original_url"])

    previous_link = (
        f'<a class="sequence-link previous" href="{previous["slug"]}.html"><span>← 上一题</span><strong>{html.escape(str(previous["title"]))}</strong></a>'
        if previous
        else '<span class="sequence-link disabled"></span>'
    )
    following_link = (
        f'<a class="sequence-link next" href="{following["slug"]}.html"><span>下一题 →</span><strong>{html.escape(str(following["title"]))}</strong></a>'
        if following
        else '<span class="sequence-link disabled"></span>'
    )

    return f"""{page_head(f'{title} · PuzzleCat 题解', f'{title}（{puzzle_id}）的独立题解与验证。', '../')}
<body class="detail-page">
  {topbar('../')}
  <main class="detail-main">
    <nav class="breadcrumb"><a href="../index.html">题解全集</a><span>/</span><span>{number:03d}</span></nav>
    <article class="solution-document">
      <header class="detail-hero">
        <div class="detail-kicker"><span>{number:03d} / 289</span><code>{puzzle_id}</code></div>
        <h1>{html.escape(title)}</h1>
        <div class="detail-actions">
          <div class="answer-panel"><span>最终答案</span><strong>{html.escape(answer)}</strong></div>
          <a class="source-button" href="{html.escape(original_url, quote=True)}" target="_blank" rel="noreferrer">打开 PuzzleCat 原题 <span>↗</span></a>
        </div>
        <dl class="local-metadata">
          <div><dt>本地结果</dt><dd>correct</dd></div>
          <div><dt>错误提交</dt><dd>{incorrect}</dd></div>
          <div><dt>整理依据</dt><dd>题面归档、solve-log、提交记录</dd></div>
        </dl>
      </header>
      <div class="detail-content">{puzzle['html']}</div>
    </article>
    <nav class="sequence-nav">{previous_link}{following_link}</nav>
    <div class="back-index"><a href="../index.html">查看全部 289 道题目</a></div>
    <footer><p>PuzzleCat 独立题解 · {html.escape(title)}</p><a href="#top">返回顶部 ↑</a></footer>
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
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    puzzle_links = json.loads(PUZZLE_LINKS.read_text(encoding="utf-8"))
    intro_html, puzzles = parse_source(
        SOURCE.read_text(encoding="utf-8"),
        metadata,
        puzzle_links,
    )
    for index, puzzle in enumerate(puzzles, 1):
        puzzle["slug"] = f"{index:03d}-{puzzle['id']}"
    ROOT.joinpath("index.html").write_text(build_index(intro_html, puzzles), encoding="utf-8")

    PUZZLE_DIR.mkdir(exist_ok=True)
    for old_page in PUZZLE_DIR.glob("*.html"):
        old_page.unlink()
    for index, puzzle in enumerate(puzzles):
        previous = puzzles[index - 1] if index else None
        following = puzzles[index + 1] if index + 1 < len(puzzles) else None
        PUZZLE_DIR.joinpath(f"{puzzle['slug']}.html").write_text(
            build_puzzle_page(puzzle, index + 1, previous, following),
            encoding="utf-8",
        )

    ROOT.joinpath("sitemap.xml").write_text(build_sitemap(puzzles), encoding="utf-8")
    print(f"Built index and {len(puzzles)} individual puzzle pages")


if __name__ == "__main__":
    main()
