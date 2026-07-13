# 9AlWHnxJ — 负负得……

- Owner: `codex-sub-h-20260712`
- Status: correct
- Incorrect submissions: 0

## Flavor / transcription

- Flavor：`为什么取两次反不等于本身？`
- 六行：`浓、胜、亲、熟、商、|` 各经两次箭头到问号，索引分别 `(3/5),(6/8),(3/5),(2/5),(11/13),(5/8)`。
- 第六行明确为 ASCII 124，即竖线 `|`。

## Mechanism

“反”读作取反义，但中间字具有不同义项，因此第二次可沿另一义项的反义词走到新字，而不返回原字：

1. `浓→淡→咸`，咸=`SALTY`，第3/5字母 `L`。
2. `胜→负→正`，正=`POSITIVE`，第6/8字母 `I`。
3. `亲→疏→密`，密=`DENSE`，第3/5字母 `N`。
4. `熟→生→死`，死=`DEATH`，第2/5字母 `E`。

前四字严格提取为 `LINE`。剩余两行继续同类多义取反并按英文长度索引，应补出 `A,R`；结合六字母唯一自然词及题目数学语境，终答候选为 `LINEAR`。

## Candidate ranking

1. `LINEAR` — 前四位严格，末两位由六字成词与数学主题唯一闭合；提交验证。

## Submissions

- `LINEAR` — correct（attempt 1，0 wrong）。

## Stopping criteria

- 若正确立即 resolve；若错误再专门重建 `商` 与 `|` 的两跳反义链，不枚举其他 LINE?? 字符串。
