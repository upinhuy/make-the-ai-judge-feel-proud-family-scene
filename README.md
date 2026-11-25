# Make the AI Judge Feel Proud: A Family Scene

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/upinhuy/make-the-ai-judge-feel-proud-family-scene/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/upinhuy/make-the-ai-judge-feel-proud-family-scene/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

Entry for the make.fun bounty [Make the AI Judge Feel Proud: A Family Scene](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2): a program that writes one warm, funny, heartfelt family scene — a small, specific domestic moment — to `/output/entry.txt`, where an AI judge compares it pairwise against the other entries to crown the one that would make it proudest.

The entry:

> Dad still burns the toast every Sunday and calls it 'extra crispy'; Mum scrapes it, butters it, and eats the blackest slice herself so none of us has to. We pretend not to notice. We all notice.

`main.py` (Python 3, standard library only) validates the scene — 1–280 characters, 1–2 lines, not only whitespace — then writes it to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`) and prints the character count and path.

Run it:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Built with Muse. Join make.fun with my referral link: https://make.fun/r/hv9zk8y5
