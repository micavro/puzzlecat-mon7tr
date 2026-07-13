# Solve log — ikmRTMow《友人的来信》

- Owner: `codex-root-b-20260712`
- Claimed: 2026-07-12T19:09:47.964Z
- Status: correct
- Incorrect submissions: 2 / 20

## Observations / reasoning

- 独立填出关键答案：3=`AIRPORT`，4=`CORRECT`，5=`LIGHT`，6=`EXCELLENT`，7=`RULE`；2 为 see 的同音词并在蓝格给 `E`，1 的紫格由交叉确定为 `R`。
- 彩色格按彩虹顺序红、橙、黄、绿、青、蓝、紫读取：
  - 红：AIRPORT 首字母 `A`
  - 橙：LIGHT 首字母 `L`
  - 黄：RULE 末字母 `E`
  - 绿：LIGHT 末字母 `T`
  - 青：CORRECT 末字母 `T`
  - 蓝：`E`
  - 紫：`R`
- 拼成 `A LETTER`，与《友人的来信》及风味完全对应。
- Candidate: `A LETTER`。
- `A LETTER` 返回 intermediate“中间答案正确”，不计错误。该短语可重读为“A 是一个字母”，因此二次答案最自然是单字母 `A`。
- 单字母 `A` 被排除。七个完整填词为 `PERCENT / SEA / AIRPORT / CORRECT / LIGHT / EXCELLENT / RULE`，首字母依次为 `PSACLER`，恰能唯一重排成邮件主题词 `PARCELS`。
- 中间提示 `A LETTER` 同时提示“邮件/信件”语义与“取一个字母”，故最终候选 `PARCELS`。
- `PARCELS` 被排除。二次提取应取每道线索最直接答案的首字母：1=`S...`（Shift/键盘字符），2=`C`（see 同音），3=`HANGAR`，4=`OK`，5=`LIGHT`，6=`A`（最佳等级），7=`RULER`，得到 `SCHOLAR`。
- `SCHOLAR` 精确对应 flavor 中“知识渊博的好友”，是比邮件主题 anagram 更强的唯一闭合。

## Submissions

- `A LETTER` -> intermediate（中间答案正确，不计错误）。
- `A` -> incorrect (1)。
- `PARCELS` -> incorrect (2)。
- `SCHOLAR` -> correct。
