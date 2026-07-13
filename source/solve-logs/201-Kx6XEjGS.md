# Solve Log: Kx6XEjGS

- Title: `月照纱窗 3`
- Owner: `recover-root-20260712`
- Status: correct
- Incorrect submissions: 4
- Answer: `枕上劝人归`

## Mechanism

- The white regions are not strokes. They are the enclosed negative spaces (the `孔`) of characters rendered invisibly on black.
- The regions fall on a 5 x 4 character grid.
- A local template matcher rendered CJK characters in SimHei/Noto Sans SC, flood-filled their enclosed counters, and compared counter count and geometry. Matching against a Chinese idiom corpus produced near-zero-error unique rows.

## Reconstructed rows

1. `枕曲藉糟`
2. `喜上眉梢`: the visible characters have two, five, and two counters; `上` is invisible.
3. `好言相劝` (or the same counter-compatible `婉言相劝`): the visible characters have two, one, and three counters; `劝` is invisible.
4. `血口喷人`
5. `解甲归田`

Each row has exactly one character with no enclosed counter, hence no white region. Reading those dark cells by row gives `枕上劝人归`, also independently found as a five-character phrase in the local Song-ci corpus.

## Submission plan

- `枕贱辩人归` - incorrect.
- `归人便见枕` - incorrect; this homophonic reversal was unnecessary.
- `枕贱分人归` - incorrect.
- `枕贱从人归` - incorrect; this exposed aspect-ratio distortion in the first matcher.
- Sister-puzzle logs confirm that this draft series submits the invisible characters directly.
- Submit corrected direct extraction `枕上劝人归` after cooldown.
- `枕上劝人归` - correct.
