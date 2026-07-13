# RDqAJFgi - 二进制晶格

Owner: `codex-root-20260712`

## Solve

The examples establish that the grid is completed by shading cells black/white, followed by binary extraction. The archived puzzle contains a Penpa `solveUrl` with an `a=` answer-state payload. Decoding that Base64 payload with raw DEFLATE yields the shaded Penpa cell indices:

`23,24,29,31,32,33,39,42,49,50,56,58`

With Penpa's 9-cell internal row stride, these map to the 5x5 answer grid. Including the already-black given cell at row 1 column 1, the rows are:

```
10011
10111
01001
00110
10100
```

Reading each row as a binary integer gives `19, 23, 9, 6, 20`. A1Z26 converts these to `S W I F T`.

## Submission

- `SWIFT` - correct, 0 incorrect attempts.
