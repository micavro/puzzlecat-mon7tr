# Solve log: 不是中文 Cryptic (`pPS2nNtD`)

Owner: `lane-b-20260712`

## Status

Recovered after one incorrect submission. Current answer: `SAGE` (high confidence).
Incorrect count: 1.

This lane did not submit, archive, resolve, or claim another puzzle.

## FPA compliance

- Solved from the archived clue and standard cryptic conventions.
- No search for an existing answer, solution, original puzzle, or WeChat source was performed.

## Clue

```text
乱世嘉人 (4)
```

The surface deliberately resembles the Chinese title of *Gone with the Wind*,
`乱世佳人`, but changes `佳` to the homophone `嘉`.

## Complete parse

```text
乱       = anagram indicator
世嘉     = SEGA (the game-company name in Chinese)
人       = definition: a person, specifically a wise person / sage
(SEGA)*  = SAGE
```

Therefore the exact answer is:

```text
SAGE
```

The enumeration is exactly four. Every character has a role: `乱` supplies the
cryptic operation, `世嘉` supplies all four letters, and `人` supplies the
definition. The `佳` -> `嘉` substitution is mechanically necessary because
`世嘉` is `SEGA`; it is not merely a decorative misspelling of the film title.

## Why `GONE` is wrong

`GONE` is strongly suggested by the film-title surface, but the site rejected
it. The proposed `G + ONE` parse is also incomplete: it must translate `嘉` as
an abbreviation for GOOD and scramble `世` = EON into ONE, while leaving `人`
without a valid definition of GONE. In contrast, `SAGE` uses the exact adjacent
unit `世嘉` and gives both a standard anagram operation and a valid definition.

## Candidate ranking

1. `SAGE` - high confidence; exact `(SEGA)*`, exact length 4, and `人` defines a sage.
2. `AGES` - the other common anagram of SEGA, but `人` cannot define AGES.
3. `GONE` - rejected by the site and lacks a valid role for `人`.
4. `WIND` - fits only the movie reference and has no cryptic wordplay support.

## Submission history

- `GONE` - incorrect, submitted 2026-07-12T18:13:16.167Z by the existing worker workflow.
- No submission from this recovery lane.

Incorrect count: 1.

## Stopping criteria

Report `SAGE` and the full `乱 + 世嘉 + 人` parse to the root worker. Do not
archive, submit, resolve, or claim another puzzle from this lane.
