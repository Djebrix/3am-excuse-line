# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Djebrix/3am-excuse-line/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Djebrix/3am-excuse-line/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

One line from a hardware wallet refusing to sign a transaction at 3 AM. Entry for [The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) on make.fun.

> It's 3 AM. My secure element is on its union-mandated nap — come back at sunrise with a decision your morning self would sign.

## Run

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` is stdlib-only, no network, and deterministic: it writes the same line to `$ENTRY_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) on every run.
