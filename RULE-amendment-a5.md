# RULE amendment: run a4 void, one repeat (a5)

Written 2026-11-16T20:39:42Z, before run a5 starts. RULE.md stays frozen and unchanged (sha256 in RULE.frozen); this file only adds
one void-and-repeat case that its «Not testable» list did not foresee.

- **What happened:** run a4 (job A, Fable 5.2) rendered its deliverable at 43.7 min, inside the 60 min cap. Its final
  check then ran 1,696 s (the other three job A runs: 10 to 224 s, from the host job log, not published) because the
  director ran the scorer on the same host while the contestant was still working, with a GPU batch sharing the host. The
  agent ended at 72.8 min and the harness scored it «finished but over the cap». The director also failed to stop the
  agent at cap + 2 min.
- **Why this is an instrument fault:** the load came from the director's own jobs, not from the contestant; a1, a2 and a3
  did not meet it. It is the same kind of case as the listed «host kills a run's process for memory that the run did not
  use».
- **Who decided:** the person, 2026-11-16T20:34:14Z: «Repetirla una vez». The director runs on
  Fable 5.2 (a contestant) and did not decide; it recommended the repeat and said so on the card.
- **The repeat:** one run, id a5, job A, Fable 5.2, the prompt file from `harness/new_run.sh a5 A` pasted whole, same
  caps (60 active min, 4 renders). Quiet host: no scorer, no GPU job and no other heavy job until the agent has ended;
  the scorer runs once, after the end. The director stops the agent at cap + 2 min.
- **No second repeat.** Whatever a5 does is scored as it is. If a5 itself is hit by a listed «Not testable» case, the
  episode says so and job A is reported with three runs.
- **Reporting:** a5 replaces a4 in the job A verdict and in the blind set. a4 stays on disk and in runs.csv, and
  RESULTS.md and the episode say that one Fable run was repeated, why, and what a4's numbers were. The number of scored
  runs stays 2 per model per job.
