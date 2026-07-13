# Solve log: OA2iZO0v

## Coordination

- Owner: `codex-sub-c-20260712`
- Title: `又是三个词？`
- Existing archive inspected; archive was not repeated.
- Incorrect submissions: 2
- Status: solved

## Observations

- The table contains 18 English what3words addresses, split into two columns and row groups of 3, 2, and 4.
- Flavor: `无处不在的坐标们，是否也会将中英谜题尽数索引？`
- Direct access to `what3words.com` returned CloudFront 403, but the official `map.what3words.com` mirror exposed coordinates in `__NEXT_DATA__`.
- Requesting each coordinate from the mirror with the `zh_si` locale yielded a Chinese three-word address. The Chinese addresses form short clues rather than arbitrary locations.

## Derivation

Each row's left Chinese address clues a phrase. The right Chinese address gives its index, except where the clue explicitly says no number or to use the phrase's own number.

1. `典故.音乐.两人` -> `高山流水`; `最小.正的.整数` -> 1; extract `高`.
2. `道德.成绩.也好` -> `品学兼优`; `很多.作文.相同` -> `千篇一律` -> 1; extract `品`.
3. `合并.杉木.杉木` -> `木质`; `多少.老虎.力量` -> `九牛二虎之力` -> 2; extract `质`.

The first group is `高品质`.

4. `冬天.传递.火种` -> `雪中送炭`; `搬家.搬家.搬家` -> `孟母三迁` -> 3; extract `送`.
5. `额外.单个.方块` -> `别具一格`; `使用.本身.索引` says to use the phrase's own `一` -> 1; extract `别`.

The second group is `送别`.

6. `模仿.吹奏.乐器` -> `滥竽充数`; `笔墨.纸张.砚台` -> `文房四宝` -> 4; extract `数`.
7. `手提.空子.字谜` is the character construction `扌 + 空 = 控`; `这次.没有.数字` says there is no index.
8. `突然.想到.方法` -> `灵机一动`; `最小.素质.数字` (smallest prime number) -> 2; extract `机`.
9. `一起.睡眠.区别` -> `同床异梦`; `人类.眼睛.数量` -> 2; extract `床`.

The third group is `数控机床`.

The resulting Chinese what3words address is `高品质.送别.数控机床`. It resolves to `(36.311408, -111.521837)`. Converting that square back to English gives `submit.answer.blueprint`, which instructs the final answer `BLUEPRINT`.

## Submissions

- `WHAT3WORDS` -> incorrect, generic response.
- `39.818362,163.818152` -> incorrect, generic response.
- `BLUEPRINT` -> correct.

## Final answer

`BLUEPRINT`
