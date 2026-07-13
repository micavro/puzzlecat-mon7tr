# Solve log: RKhAJFgi

## Puzzle

- Owner: `codex-sub-ab-20260713`
- Title: `神鲸谜 007`
- Image shows two Wordle-style five-cell guesses and a three-Chinese-character answer enumeration.
- Cooldown: 1 minute; incorrect limit: 50.

## Mechanism

Treat the visible glyphs as pieces rather than as ordinary Chinese/English words.

- First guess `一 去 二 三 里`: `一` is green (correct position); `三` is yellow (present, wrong position); the other three are absent.
- Second guess `CACHE`: both `C` cells and `H` are yellow; `A/E` are absent.

Thus the hidden five-cell string consists exactly of `一、三、C、C、H`, with constraints:

- position 1 is `一`;
- `三` is not position 4;
- the two `C`s are not positions 1 or 3;
- `H` is not position 4.

The chemically meaningful arrangement is uniquely:

```text
一 C 三 C H
— C ≡ C H
```

That is the structural fragment `—C≡CH`, the ethynyl group. The requested three-character Chinese answer is `乙炔基`.

## Candidate ranking

1. `乙炔基` — confidence 0.999; satisfies every Wordle position/count constraint and exactly names the five-piece structural formula.

## Submissions

- `乙炔基` — correct. Final incorrect count: 0.

## Stopping criteria

Stopped on the correct verdict for `乙炔基`.
