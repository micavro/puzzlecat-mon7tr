# JumgoAEX - 以德芙人

Owner: `chat2-root-20260712`

## Observations

- Three Chinese words share the missing prefix `滑`: 滑梯、滑冰、滑翔.
- Five English slots are provided for each row, and a blue ski trajectory crosses one
  slot per row.

## Reasoning

- 滑梯 -> `SLIDE`.
- 滑冰 -> `SKATE`.
- 滑翔 -> `GLIDE`.
- The blue path crosses row positions 1, 2, and 3 respectively, extracting `S`, `K`,
  and `I`.
- `SKI` is confirmed by the skier at the start of the path and the `ANS` marker.

## Candidate ranking

- `滑雪` - checker-requested Chinese translation of the supported intermediate `SKI`.

## Submissions

- `SKI` - recognized intermediate: `对啦~那么这个词的中文是……？` (`0` incorrect).
- `滑雪` - correct (`0 / 20` incorrect).

## Stopping criteria

- Resolve correct if `SKI` is accepted.

Resolved `correct` with answer `滑雪`.
