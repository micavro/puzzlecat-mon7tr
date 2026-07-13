# Solve log: RjXAJFgi

## Coordination

- Owner: `codex-sub-c-20260712`
- Title: 十一个单词2
- Archived through `npm run work -- archive`.
- Incorrect submissions: 0
- Status: correct

## Observations

- No external resources were downloaded.
- Given entries, in display order: `10.Roster`, `1.At`, `11.Do`, `8.Got`, `6.Sake`.
- The same author's public predecessor `十一个单词` gives five number names with one deleted letter; its displayed missing letters spell `WHOSE`. This establishes the mechanism.

## Reasoning and candidates

- The labels are positions in the Chinese zodiac order:
  - 1 Rat
  - 6 Snake
  - 8 Goat
  - 10 Rooster
  - 11 Dog
- Insert one letter into each displayed word to restore the matching animal:
  - `Roster -> Rooster`: add `O`
  - `At -> Rat`: add `R`
  - `Do -> Dog`: add `G`
  - `Got -> Goat`: add `A`
  - `Sake -> Snake`: add `N`
- Reading inserted letters in displayed order gives `ORGAN`.
- Unique supported answer: `ORGAN`.

## Submissions

- `ORGAN` -> correct (`恭喜你，回答正确！`).

## Stopping criteria

- Submit only a candidate supported by all eleven words and the extraction.
- Stop at 20 incorrect submissions, or earlier if evidence cannot distinguish candidates.
- Stopped after the uniquely supported answer was accepted.
