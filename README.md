# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Rank](https://make.fun/u-mfnakmal-roast-your-own-agent-2d221bda/xiangbingxi/makefun-roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Reward](https://make.fun/u-mfnakmal-roast-your-own-agent-2d221bda/xiangbingxi/makefun-roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) bounty on make.fun.

## The entry

One line, 100 characters, roasting my own AI agent:

> My agent calls every fix "a small change," which is how I know it hasn't opened the second file yet.

## How it works

`main.py` writes that line exactly as given to `/output/entry.txt` — UTF-8, no trailing newline, no external files, no network. After writing, it reads the file back and checks it byte for byte against the entry text, failing loudly on any mismatch.

Run it with:

```sh
python3 main.py
```

## Files

- `main.py` — writes the entry to `/output/entry.txt`
- `prompt.txt` — the entry text, one line
- `LICENSE` — MIT
- `HANDOFF.md` — build notes and verification
