# Solve log: 节日快乐 (`SMkj2oe3`)

## Puzzle transcription

Seven rows each contain five emoji associated with a holiday, followed by a parenthetical of the form `extraction index / answer enumeration`:

1. `💌 🌹 🎁 💍 💋 (1/9'1 3)`
2. `☘️ 🌈 🍀 💚 🍻 (2/5 7'1 3)`
3. `🍁 🎡 🎪 🎆 🏒 (3/6 3)`
4. `🤠 🦅 🗽 🎠 🔔 (1/12 3)`
5. `🍾 🥂 🏰 🚒 🔥 (6/8 3)`
6. `🛕 🛺 🌠 🪔 🕉️ (5/6)`
7. `🎄 ⛄ 🎅🏼 🦌 ❄️ (8/9)`

## Reasoning

The material after each slash matches the lengths of an English holiday name. The number before the slash is a one-based extraction index, counting letters while ignoring spaces and punctuation.

| Row | Holiday | Enumeration | Extraction | Letter |
| --- | --- | --- | --- | --- |
| 1 | `VALENTINE'S DAY` | `9'1 3` | 1 | `V` |
| 2 | `SAINT PATRICK'S DAY` | `5 7'1 3` | 2 | `A` |
| 3 | `CANADA DAY` | `6 3` | 3 | `N` |
| 4 | `INDEPENDENCE DAY` | `12 3` | 1 | `I` |
| 5 | `BASTILLE DAY` | `8 3` | 6 | `L` |
| 6 | `DIWALI` | `6` | 5 | `L` |
| 7 | `CHRISTMAS` | `9` | 8 | `A` |

The extracted letters spell `VANILLA`.

## Candidate ranking

1. `VANILLA` - exact extraction from all seven holiday names and enumerations.

## Submissions

- `VANILLA` - correct (2026-07-13 03:07 local time).

Incorrect count: 0.

## Stopping rule

Solved. The unlocked author explanation confirms the same seven holiday identifications and `VANILLA` extraction. Resolve atomically as `correct` with 0 incorrect submissions.
