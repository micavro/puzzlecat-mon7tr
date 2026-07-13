# Solve log: 课文两景

- Puzzle ID: `TkqKhwRH`
- Owner: `codex-sub-b-20260712`
- Status: correct
- Incorrect submissions: 0

## Observations

- The image contains two rows of three colored-bar groups. The black marks over individual bars are the four Mandarin tone marks, so each group represents a pinyin syllable; equal colors represent equal letters.
- Upper row patterns decode as `shuǐ lián dòng`:
  - `shuǐ` and the lower row's six-letter first syllable share `shu`.
  - `lián` shares its initial with lower `lóng`.
  - `dòng` is identical in both rows.
- This gives `水帘洞`, a scene in the fifth-grade People's Education Press text `猴王出世`, matching the stated membership in 五年级课文.
- Lower row decodes as `shuāng lóng dòng`, giving `双龙洞`, from the fourth-grade text `记金华的双龙洞`, matching 四年级课文.
- The boxes align under the three decoded characters. Label `1` is under `水`; label `2` is under `龙`; the cyan boxes mark the shared `洞`. Reading labels 1 then 2 extracts `水龙`.

## Candidate ranking

1. `水龙` - strong and mechanically extracted from the two numbered character positions.
2. `水帘洞双龙洞` - the two decoded scenes, but the numbered boxes explicitly indicate a shorter extraction.

## Submissions

- `水龙` - correct at `2026-07-12T20:08:28Z`; extracted from the numbered positions in `水帘洞` and `双龙洞`.

## Stopping criteria

- Submit only the numbered extraction first.
- Stop after 20 incorrect submissions, or classify `cannot_do` earlier if later evidence cannot distinguish candidates.
