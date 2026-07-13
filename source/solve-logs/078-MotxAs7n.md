# Solve log: MotxAs7n - 七字谜

- Owner: `lane-c-20260712`
- Claimed: 2026-07-12T09:33:23.442Z
- Status: correct
- Incorrect submissions: 0
- Submitted answers: none

## Observations

- Puzzle is tagged `字谜`, `交互`, and `交互谜题`.
- Archived through the coordinated browser workflow; no external resources were downloaded.
- The interactive asset is a single text input with placeholder `接醉里挑灯看剑`; it has no JavaScript. Its only mechanism is a custom embedded OpenType font named `PuzzleFont`.
- The embedded font is based on Source Han Sans CN Normal 2.005 and contains 30,939 glyphs. A same-version official Source Han Sans reference was downloaded for reproducible outline comparison.
- `analyze_font.py` hashes the resolved vector outline for every common Unicode codepoint. It found a small set of deliberately replaced Chinese glyphs amid an otherwise ordinary font.
- Rendering the altered glyph for `赢` produces a bespoke two-line underlined message: `FONT` / `MASTER`, not the Chinese character.

## Reasoning

The font substitutions turn a correct response into the next clue. The recovered opening chain is:

1. `接醉里挑灯看剑` asks for the continuation of the verse. Entering `梦回吹角连营` renders `逆法语文中学`.
2. `逆法语文中学` means reverse `法语文中学`, giving `学中文语法`. Entering that renders `半莱阳旁张`.
3. `半莱阳旁张` asks for the useful halves/components of `莱 阳 旁 张`: `来 日 方 长`. Entering `来日方长` renders `对文收徒`.
4. The remaining deliberately replaced characters continue this character-operation chain. Full traversal is not needed to identify the platform answer because the terminal `赢` glyph itself has a unique, explicit English rendering.

The terminal message is especially strong evidence: `FONT MASTER` describes exactly the custom-font construction used by the puzzle and is not a generic success symbol or an inferred synonym.

## Candidate ranking

1. `FONT MASTER` - explicit text drawn by the handcrafted terminal glyph; overwhelmingly preferred.
2. `FONTMASTER` - normalization-equivalent spelling without the displayed space, unnecessary because the platform strips spaces.
3. `赢` - merely the input codepoint that reveals the terminal message, not the message itself.

## Submissions

- `FONT MASTER` - correct (`2026-07-12T09:42:13.322Z`); incorrect count remains 0.

## Resolution

- Outcome: `correct`
- Accepted answer: `FONT MASTER`
- Incorrect submissions: 0

## Stopping criteria

- Submit only answers supported by the interaction mechanism and an explicit extraction.
- Stop at 20 incorrect submissions, or earlier as `cannot_do` if archived evidence and reproducible interaction no longer distinguish candidates.
