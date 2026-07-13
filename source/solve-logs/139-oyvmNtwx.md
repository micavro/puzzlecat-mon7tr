# Solve log: oyvmNtwx

## Puzzle

- Owner: `recover-w2-20260712`
- Title: 好数
- Need construct a 27-digit good number containing digits 1-9 and decode `风清月明`.

## Good-number rule

For every digit `d`, consecutive occurrences are exactly `d+1` positions apart, i.e. there are exactly `d` intervening digits. Every digit used must occur at least twice.

Examples:

- In `312132`, the two 1s, 2s, and 3s are separated by 2, 3, and 4 positions respectively.
- `30003` is valid: the 3s differ by 4 positions, while consecutive 0s are adjacent.
- `121` is invalid because 2 occurs only once.

An initial search incorrectly assumed every digit occurs exactly three times. General exact-cover search with the character constraints allows nine valid completions, but all give the same queried component values.

## Character structure

The 22 displayed symbols expand to 27 digits because exactly five characters have left-right structure and therefore encode two component digits:

- `清 = 氵 + 青`
- `河 = 氵 + 可`
- `时 = 日 + 寸`
- `晴 = 日 + 青`
- `对 = 又 + 寸`

The other displayed Chinese characters encode a single component digit. This gives consistency constraints such as the second digit of 清 equaling 青, both 晴 and 时 starting with 日, and both 时 and 对 ending with 寸.

These constraints force 氵=1, 青=8, 日=2, and 寸=6. General search gives nine completions, beginning with either `181215...` or `181915...`; the differences do not affect the requested characters. One valid completion is:

`181215267285296475384639743`

The decoded character values are:

- 清=18 (河 can vary between compatible values)
- 月=5
- 时=26, 风=7, 晴=28
- 日=2, 寸=6, 青=8, 对=46

Since `明 = 日 + 月`, its two-digit value is `25`. Therefore:

`风清月明 = 7 / 18 / 5 / 25`

The four values `7,18,5,25` are A1Z26 indices:

- 7 = G
- 18 = R
- 5 = E
- 25 = Y

Thus the `(4)` answer is `GREY`. The numeric submission omitted this final conversion.

## Candidate ranking

1. `GREY` - A1Z26 conversion of the four decoded character values.

## Submissions

- `718525` - incorrect; these are intermediate A1Z26 indices, not the enumerated four-letter answer. Incorrect count: 1.
- `GREY` - correct. Final incorrect count: 1.

## Stopping criteria

Stopped on the correct verdict for `GREY`.
