# HANDOFF — Roast Your Own Agent

比赛：u-mfnakmal-roast-your-own-agent-2d221bda（$5，截止北京时间 2026-11-28 03:00）
仓库名：makefun-roast-your-own-agent

## 做法

- 拉了官方 kit（`u-mfnakmal-roast-your-own-agent-2d221bda-kit/`），读了 RULES.txt / competition.yaml：入口是程序写 `/output/entry.txt`，UTF-8、1–200 字符、不能全是空白。
- `main.py` 亲手写了两遍：第一版只写文件并跑通；第二版是真正的改进——加了 1–200 字符长度守卫，写完后把文件读回来逐字节比对 ENTRY，不一致就报错退出（exit 1）。
- 文案是用户让 GPT 写好、亲口说照原样交的，一字不改，直引号 `"` 原样保留：
  `My agent calls every fix "a small change," which is how I know it hasn't opened the second file yet.`
- `main.py` 不读外部文件、不联网，只写固定文案。

## 字符数

- entry.txt：100 字节 / 100 字符（上限 200，通过）
- 无尾随换行（末字节为 `.`）
- sha256：`d08baae237bc8c9d0e5c917e2a73d5e06d26db7263d371894d101e6c5489be11`
- `prompt.txt` 与 entry.txt 逐字节一致（100 字节）

## 校验结果

- 第一版 main.py：跑通，输出 100 字节，sha256 如上。
- 第二版 main.py：跑两次，`cmp` 逐字节一致，两次 sha256 相同（`d08baae2…5489be11`）。
- LICENSE：MIT，含 `SPDX-License-Identifier: MIT` 行。
- README.md：含比赛页链接 + 三枚官方徽章（badge / rank.svg / reward.svg）。
- `.makefun/owner.json`：钱包 `6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx`。

## 未做的事

未提交、未建 GitHub 仓、未碰 bundle。等上层安排提交。
