# FbXyul5g - 地名重组

Owner: `chat2-root-20260712`

## Observations

- Archive completed with 12 files and no failed resources.
- The image uses three consistently colored blank blocks. The final line asks
  for the provincial capital of the place made by light + medium + dark, with
  Chinese enumeration `(三)`.
- The puzzle metadata's author-supplied wrong-answer hint says: `每个色块代表两个字母！`
  (each colored block represents two letters).

## Reasoning

- Initial `FU/JI/AN -> FUJIAN` hypothesis was falsified by all three direct
  representations of Fuzhou and, critically, did not explain the literal `a`
  or the geographical membership line.
- The complete mapping is light=`SH`, medium=`AN`, dark=`XI`:
  - light + medium = `SHAN`, the pinyin for 山, exactly matching the mountain icon.
  - dark + medium = `XI` + `AN` = `XIAN` (西安).
  - light + literal `a` + medium + dark = `SH` + `a` + `AN` + `XI`
    = `SHAANXI` (陕西), and Xi'an is indeed in Shaanxi.
  - light + medium + dark = `SHANXI` (山西).
- Shanxi's provincial capital is Taiyuan. The `(三)` enumeration points to the
  three-character administrative name `太原市`.

## Candidate ranking

- `太原市` - uniquely follows the full SH/AN/XI mechanism and `(三)` enumeration.

## Submissions

- `福州市` - incorrect (`2026-07-12T11:55:00.775Z`). This rejects the
  three-Chinese-character administrative-name interpretation of `(三)`.
- `FUZHOU` - incorrect (`2026-07-12T11:57:08.207Z`). This rejects the
  Latin/pinyin form despite the letter-based mechanism.
- `福州` - incorrect (`2026-07-12T12:00:16.982Z`). Together, the three Fuzhou
  forms falsify the initial FU/JI/AN hypothesis.
- `太原市` - correct (`2026-07-12T12:04:43.589Z`).
- Total incorrect: `3 / 20`.

## Result

- `correct`: `太原市`.

## Next controlled test

- `太原市`: derived from SHANXI after the XIAN-in-SHAANXI cross-check. Test only
  after cooldown.

## Stopping criteria

- Resolve `correct` after an accepted, mechanism-supported answer.
- Resolve `cannot_do` if evidence cannot distinguish candidates.
- Resolve `wrong_20` after exactly 20 incorrect submissions.
