# Solve log: Xe7kPIap / 无需枚举

## Claim

- Owner: `route-a-20260712`
- Claimed: 2026-07-12
- Status: correct
- Incorrect submissions: 0

## Observations

- Title: 无需枚举 (roughly "No Need to Enumerate")
- Tags: 一枚, 英文
- Initial archive contains no separately downloaded resources.
- Flavor text says the number before the slash is the extraction position and the number after it represents the word or phrase to extract from.
- Puzzle body: `(1/5 4) (3/4) (5/7 4)`.

## Reasoning

- The apparent enumerations after each slash identify English number names without any external clue:
  - `5 4` is the enumeration of `FIFTY FOUR`, i.e. the number 54 written in English.
  - `4` is the enumeration of `FOUR`, i.e. the number 4 written in English.
  - `7 4` is the enumeration of `SEVENTY FOUR`, i.e. the number 74 written in English.
- Apply the extraction index before each slash, ignoring spaces:
  - 1st letter of `FIFTY FOUR` = `F`.
  - 3rd letter of `FOUR` = `U`.
  - 5th letter of `SEVENTY FOUR` = `N`.
- Extraction gives `FUN`, an English answer and a fully self-confirming use of every datum.

## Candidate ranking

- `FUN` - decisive; exact extraction and thematic fit.

## Submissions

- `FUN` - correct (`2026-07-12T06:46:09.531Z`); site message: `恭喜你，回答正确！`.

## Stopping criteria

- Submit only candidates supported by a reproducible extraction or a strong self-confirming mechanism.
- Stop after 20 incorrect submissions; stop earlier as `cannot_do` if evidence cannot distinguish candidates.
