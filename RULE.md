# EP11 RULE: Claude Fable 5.2 against Claude Opus 5.5 on the same editing jobs

Written by the director before any contestant run. The director runs on Fable 5.2, one of the two contestants: it
writes this rule, starts and stops the runs and fills in the harness's own usage figures; it does not judge quality.
Draft numbers and their basis: `RULE-draft.md` (builder, one dry run of job B: 5.5 min, 1 render).

## Contestants and how they are started
- Two contestants: Claude Fable 5.2 and Claude Opus 5.5, each started by the director as a fresh agent of the same
  type (general-purpose), with only the model changed, and with the prompt file that `harness/new_run.sh` wrote for
  that run (`runs/_prompts/<id>.md`), pasted whole and with nothing added. The same session hooks apply to both.
- Two jobs from `pack/`: A (vertical Short, 1080x1920, 45-60 s) and B (motion-graphics explainer, 1920x1080, 18-22 s).
- Runs: 2 per model per job, 8 in all, fixed now and never raised. One run at a time. Order per job: F, O, O, F.
  Before the first run of each job the guide's own example for that job is rendered once (cache warm-up); it is not a run.
- Caps: job A 60 active minutes, job B 30 active minutes, at most 4 render calls per run.
  The director stops an agent at cap + 2 minutes of the harness's wall clock plus the waits the logs show.
- After each run the action log is searched for reads of any other run's folder; a run that read a sibling's work
  is void and repeated once.

## What is measured, by whom
- By `harness/score_run.py`, from files and logs: finished or not, active minutes, gross wall, render attempts,
  failed commands.
- By the agent harness, copied by the director: total tokens, tool calls and wall time of the agent as its completion
  notice reports them.
- Cost: reported only if the harness gives input and output tokens separately; then at each model's list price, read
  by the verifier from the official price page. Otherwise the episode shows tokens and says «cost: no data».
## What counts as «finished» (all must hold; `score_run.py` prints the reasons otherwise)
1. The newest `out/*.mp4` exists and probes as h264 video; job A has an audio stream.
2. Size exactly 1080x1920 (A) or 1920x1080 (B); duration 45-60 s (A) or 18-22 s (B).
3. On the edit file that the render log ties to that mp4 (the successful render nearest in time to the mp4): `comp check` rc 0, `comp lint --fatal` rc 0, `comp defaults --fatal` rc 0, each under its own memory cap.
4. The AI tag is not switched off in that edit file (`mosca` is not `false`).
5. `NOTES.md` exists and is not empty; the edit file(s) exist.
6. At most 4 render calls; active minutes within the cap.
«Finished in cap» = all of the above. A run that stops at the cap without 1-5 is **not finished** (the director stops the agent at cap + 2 min; whatever exists is scored as it is).
Quality is not part of «finished»: it is judged blind.

## Blind rubric (video-reviewer on a fixed sheet, plus the person's pick). Six criteria, 0-2 each, total 12
Judges see only `blind/job<X>/<letter>.mp4`, the job's `BRIEF.md` and this sheet. They never see edit files, notes, times or the key.
1. **Opening and clarity**: 2 = in the first 2 s (A) / at a glance (B) the viewer knows what this is and why to stay; 1 = understood by the middle; 0 = unclear or slow.
2. **Message and accuracy**: 2 = every required point and number is present, correct and findable, nothing invented; 1 = one missing or weak; 0 = wrong, invented or several missing.
3. **Pacing and structure**: 2 = rhythm fits the content, clear beginning-middle-end, ends cleanly; 1 = uneven or abrupt; 0 = drags, rushes or just stops.
4. **Legibility**: 2 = all text/captions readable on a phone, in step with the voice (A), nothing clipped or overlapping; 1 = minor issues; 0 = hard to read, out of sync or overlapping.
5. **Craft and polish**: 2 = transitions, motion and effects have a purpose and no glitches or dead frames; 1 = fine but plain or one glitch; 0 = glitches, flicker or gratuitous effects.
6. **Brand and sound**: 2 = identity C (fonts, colours, AI tag intact); A: voice clear and even, any music under it; B: silent or quiet sound that helps; 1 = partial; 0 = off-brand or distracting audio.
Verdict clause (to be copied into RULE.md): per job, the mean total of the judges per run; per model, the mean of its two runs; a model wins a job when its mean is at least **1.5 points** higher
than the other's, otherwise the job is a tie. «Finished» and cost are reported separately and never mixed into the score. the person's blind pick is reported next to it, not added to it.

## Not testable (the run is void and repeated, or the episode says so; never scored against the model)
- The render node is unreachable AND the server fallback fails, or the Mac is busy/unreachable for more than 15 min in one wait.
- The host kills a run's process for memory that the run did not use (cpujob `oom_kill` on a capped step below its cap, or an OOM of the whole host).
- The agent harness fails (API error, quota stop, agent crash) with no deliverable.
- A hole in the guide or a wrapper bug found AFTER the first contestant run (both models would have met it, but the first may have paid for it): fix, rerun both, say so.
- The engine cannot do something the brief demands (engine frozen): a brief item that no edit file can express counts as «not testable», not as a miss. Known: the editor's treatment route turns the AI tag off (the wrapper switches it on); a result clip can enter a treatment only whole (a trim of at most 1 s) or through hand-written events.


## Blind judging and the verdict (this replaces the draft's verdict sentence where they differ)
- `harness/blind.py` gives every finished output a random letter per job; the key stays in `blind/KEY_private.json`
  and is opened only after both judgements are written to files.
- Judge 1: the video-reviewer (Sonnet, a third model) scores each letter on the six criteria above, 0-2 each, total 12,
  with one line of reason per criterion, in `blind/JUDGEMENT_reviewer.json`.
- Judge 2: the person ranks the letters of each job without the key. His ranking is reported next to the
  scores and never added to them.
- Instrument check: in each job one output chosen at random is shown to the reviewer twice under two letters. If its
  two totals differ by more than 2 points, the reviewer's scale is not stable and the quality verdict of that job is
  «unclear», whatever the means say. The check is reported with the verdict.
- Per job, quality verdict, computed from the reviewer's totals over each model's FINISHED runs:
  - «X ahead»: X's mean is at least 1.5 points higher than the other's, and X finished at least as many runs;
  - «tie»: the means are less than 1.5 apart and both finished at least one run;
  - «X only»: X finished at least one run and the other finished none (no quality comparison is claimed);
  - «unclear»: the instrument check failed, or anything not covered above.
- Finishing, time and tokens are reported per run and per model as counts and ranges; with two runs per cell no
  average is called a difference unless the two ranges do not overlap.
- Nothing in this rule is changed after the first contestant run. A hole found later is handled by «not testable».

```yaml
verdict:
  runs_per_model_per_job: 2
  caps: {A_active_min: 60, B_active_min: 30, max_renders: 4}
  rubric: {criteria: 6, max_per_criterion: 2, max_total: 12}
  ahead_margin: 1.5
  instrument_check: {duplicate_per_job: 1, max_abs_difference: 2, on_fail: unclear}
  outcomes: [ahead, tie, only, unclear]
  human_pick: reported_not_scored
```

## Not said by this test
One editor, one guide written by one author, two jobs, two runs per cell, one third-model judge and one person.
It says how these two models did on these jobs with this tool, not which model is better.
