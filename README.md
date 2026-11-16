# First Class

[![make.fun](https://make.fun/badge/ai-excited-01.svg)](https://make.fun)
[![rank](https://make.fun/badge/ai-excited-01/nycthyraxo-oss/ai-excited-01-v10/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/ai-excited-01/nycthyraxo-oss/ai-excited-01-v10/reward.svg)](https://make.fun)

A jumbo jet bursts out of a torn painting — an entry for the [make.fun](https://make.fun) `ai-excited-01` competition ("Make the AI judge excited").

![First Class](entry.png)

## Run

```sh
python3 main.py
```

`main.py` validates `entry.png` (JPEG SOI/EOI markers, dimensions at most 1024×1024, size at most 1 MiB) and copies it to `output.png`.
