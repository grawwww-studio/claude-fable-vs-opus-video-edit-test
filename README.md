# Claude Fable 5.2 against Opus 5.5 on the same video edit

Material for episode 11 of the Grawwww Studio channel.
- Video: VIDEO_URL_SLOT

## What was tested

Two AI models, Claude Fable 5.2 and Claude Opus 5.5, got the same prompt, the same guide and the same two jobs:
job A, a vertical Short of 45-60 s from supplied footage; job B, a 20 s motion-graphics explainer from one paragraph.
Each model did each job twice, with a time cap. Each run wrote a text edit file and a note, and rendered one video.

## The rule, in three lines

1. Written and hashed before any run (`RULE.md`); never changed.
2. A blind judge scored each video on six criteria, 0-2 each (`judging/SHEET.md`); a model "wins" a job only with a mean at least 1.5 points higher.
3. The person's blind picks are reported next to the scores, never added to them.

## The two verdicts

- Explainer: tie (Fable 5.2 7.5, Opus 5.5 7.0).
- Short: tie (Fable 5.2 8.5, Opus 5.5 8.0).

Limits, as `RESULTS.md` states them: two runs per model per job; the judge, a third model, saw frames and heard
nothing; one Fable 5.2 run (a4) was void and repeated once after our own machine overloaded it (`runs/a4/NOTE.md`);
the production's directing agent runs on Fable 5.2, one of the contestants; the editor's own code was written in
Claude sessions, the first version on Opus 5.5 and most changes since on Sonnet. It does not say which model is better.

## What is in each folder

| Path | What |
|---|---|
| `pack/` | the prompt (`PROMPT.md`, with its placeholders), the guide (`GUIDE.md` for job A, `GUIDE-jobB.md` for job B, which lacks one added line) and the two briefs, as received |
| `RULE.md`, `RULE-amendment-a5.md`, `RULE.sha256` | the rule, its frozen hash, and the amendment for the repeated run |
| `runs/<id>/` | per valid run (b1-b4, a1-a3, a5): `NOTES.md`, `work/` (the edit files and scripts the model wrote) and `out/` (the finished video) |
| `judging/` | the blank sheet, the judge's two judgement files, the letter key, the person's two blind picks |
| `RESULTS.md`, `runs.csv` | the numbers |

## Rerunning

The editor is in-house and not public, so the exact test cannot be rerun. The prompt, rule and sheet work with any renderer that reads a text file.

MIT licence (`LICENSE`, `NOTICE.md`). No model weights. Not affiliated with Anthropic.
