# EP11 RESULTS

> Public copy. Files referred to here live in this repo as `judging/` (the blind sheet, judgements and key), `runs/<id>/`
> (notes, edit files, videos) and `runs.csv`. Only the person's name, review-card ids and internal log paths were removed.
> Files named «not published» (the action log, host job log) are not in this repo.

Rule: RULE.md, frozen 2026-11-16T01:33:55Z (sha256 aa1ea3f0…0ff85). Numbers: runs.csv (harness), the agent
harness's completion notices (tokens, tool calls, agent minutes), judging/JUDGEMENT_reviewer_jobB.json,
judging/JUDGEMENT_person_jobB.json. Key opened 2026-11-16T02:57Z, after both judgements were on file.

## Job B: motion-graphics explainer, 1920x1080, 18-22 s (2026-11-16, runs 01:34Z-02:22Z, one at a time, order F, O, O, F)
| run | model | finished in cap | active min | renders | failed commands | tokens | tool calls | blind letter | reviewer total /12 |
|---|---|---|---|---|---|---|---|---|---|
| b1 | Fable 5.2 | yes | 16.7 | 2 | 17 | 153,303 | 44 | G | 8 |
| b2 | Opus 5.5 | yes | 6.4 | 1 | 4 | 100,619 | 26 | C | 7 |
| b3 | Opus 5.5 | yes | 9.9 | 1 | 1 | 123,425 | 34 | D | 7 |
| b4 | Fable 5.2 | yes | 12.5 | 1 | 9 | 134,424 | 32 | J (and R, the duplicate) | 7 (and 7) |

- Finished: 2 of 2 for each model.
- Time: Opus 5.5 6.4-9.9 active minutes, Fable 5.2 12.5-16.7: the ranges do not overlap, so by the rule this is
  reported as a difference: Opus 5.5 was faster on both of its runs than Fable 5.2 on either of its own.
- Tokens: Opus 5.5 100,619-123,425, Fable 5.2 134,424-153,303: the ranges do not overlap; Opus 5.5 used fewer.
- Cost: no data (the harness reports total tokens only, not input and output separately).
- Instrument check: the duplicate (J shown again as R) got 7 and 7, difference 0 (limit 2): passed.
- **Quality verdict by RULE.md: «tie»**: reviewer means Fable 5.2 7.5, Opus 5.5 7.0, difference 0.5, under the 1.5 margin.
- The person's blind order (verbatim «D, G, R,...»): first D (Opus 5.5, b3), second G (Fable 5.2, b1), third R
  (Fable 5.2, b4, the duplicate copy); C (Opus 5.5, b2) and J (Fable 5.2, b4) not ranked. Reported, not scored.
  The reviewer's own ranking was G, J, R, D, C: the person's first choice is the reviewer's fourth.
- Common to all five outputs (reviewer): a sliced-glitch closing line and black dips between scenes; every required
  figure (600, 147, 4.1) present and correct.
- Incidents: b4 met one false block of a host guard (its NOTES.md); time lost not measured. The director saw the
  blind files' sizes before re-encoding them and so knew the mapping before the judgements; the director did not judge.
- Not said: two runs per model, one job so far, one guide by one author, one third-model judge that could not play
  video (frames at 4 fps), one person who ranked three of five.

### Job B, director's note on run b4's guard incident (2026-11-16T03:04Z; raised by the gate-1 skeptic)
- What happened: one shell command of run b4 (a here-document that wrote a script file) was refused by a host guard
  on a false match; the run then wrote the file with its file tool (its NOTES.md, line 12). Refused commands are not
  in the action log, so the loss is bounded, not measured: the longest pause before any file write in b4 is 76 s
  (02:12:38Z to 02:13:54Z; the others are 24 s and 15 s), from the action log (not published).
- Time: b4's 12.5 active minutes minus the 76 s upper bound is 11.2, still above Opus 5.5's slowest run (9.9). The
  statement «Opus 5.5 was faster on both of its runs than Fable 5.2 on either of its own» holds with the bound applied.
- Tokens: NOT safe as a non-overlap claim. b4's 134,424 against Opus 5.5's 123,425 is a gap of 10,999 tokens, and one
  repeated turn could account for that much; the harness gives no per-turn figures. To be said as: Fable 5.2 used more
  tokens in both of its runs; for one of them part of the gap may come from our own tooling, not measured.
- The 9 failed commands counted for b4 are failed editor calls (check 1, defaults 1, frame 5, lint 2, runs.csv); the
  refused shell command is not among them.
- The guide gained one line before job A so that no job A run meets the same refusal.

## Job A: vertical Short, 1080x1920, 45-60 s (2026-11-16, runs a1-a3 13:06Z-14:59Z, a5 20:40Z-21:19Z, one at a time, order F, O, O, F)
Numbers: runs.csv rows a1, a2, a3, a5 (harness), the agent harness's completion notices (tokens, tool calls), judging/JUDGEMENT_reviewer_jobA.json, judging/JUDGEMENT_person_jobA.json. Key opened
2026-11-17T01:25:46Z (first read of the key in the action log, not published), after both judgements were on file. Totals and means below were computed by script from those files.

| run | model | finished in cap | active min | renders | failed commands | tokens | tool calls | blind letter | reviewer total /12 |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Fable 5.2 | yes | 39.3 | 2 | 13 | 216,238 | 82 | V | 7 |
| a2 | Opus 5.5 | yes | 37.5 | 1 | 21 | 205,954 | 79 | U | 8 |
| a3 | Opus 5.5 | yes | 28.3 | 1 | 13 | 182,701 | 68 | G | 8 |
| a5 | Fable 5.2 | yes | 37.8 | 1 | 47 | 198,141 | 68 | F (and H, the duplicate) | 10 (and 10) |

- Run a4 (Fable 5.2) is void and was repeated once as a5: instrument fault (the director's scorer and a GPU batch
  overloaded the host during the run; its final check took 1,696 s against 9.6-56.6 s for the final checks of a1, a2, a3 and a5; it ended at 72.7 active
  minutes by runs.csv (the amendment file, frozen, says 72.8), over the 60 min cap). Written before a5 in RULE-amendment-a5.md (sha256 6bc19722…511c); the person chose «Repetirla
  una vez» (repeat it once). No second repeat. a4 stays on disk and is in no figure here.
- Finished: 2 of 2 for each model.
- Time: Opus 5.5 28.3-37.5 active minutes, Fable 5.2 37.8-39.3. The ranges do not overlap, so by the rule this is a
  difference: Opus 5.5 was faster on both of its runs (28.3 and 37.5) than Fable 5.2 on either of its own (37.8 and
  39.3). Plain fact next to it, not a grade: the closest two runs (a2 and a5) are 0.3 minutes (18 s) apart, and the
  void run a4 showed that load on our host can move a run by minutes.
- Tokens: Opus 5.5 182,701-205,954, Fable 5.2 198,141-216,238: the ranges overlap, no difference is claimed.
- Renders: Opus 5.5 1 and 1; Fable 5.2 2 and 1. Failed commands: Opus 5.5 13-21, Fable 5.2 13-47 (overlap; a5 alone 47).
- Cost: no data (the harness reports total tokens only, not input and output separately).
- Instrument check: the duplicate (F shown again as H) got 10 and 10, difference 0 (limit 2): passed. Weaker than it
  reads: the reviewer wrote that «F and H looked identical on every frame I viewed», so the second score was not blind
  to the first.
- **Quality verdict by RULE.md: «tie»**: reviewer means Fable 5.2 8.5 (7 and 10), Opus 5.5 8.0 (8 and 8), difference
  0.5, under the 1.5 margin. Both finished 2 of 2.
- The person's blind pick (verbatim «diria que la mejor es la G»): G = a3, Opus 5.5. The person named a
  first choice only; F, H, U, V not ranked. Reported, not scored. The reviewer's own ranking was F, H, G, U, V: the
  person's first choice is the reviewer's third (G and U both scored 8).
- What the reviewer noted differently: F and H put a title, the 4.1X claim and captions on screen inside the first
  1.2 s; G, U and V open on an untitled split with very small labels.
- Common to all five outputs (reviewer): a slice/glitch entrance on one or two key captions (in G and U it hides the
  caption for 1.25-2.5 s); small mono labels unreadable at phone size; 16:9 result clips shown as small tiles or heavy
  crops; a black or blank last frame after the end card.
- Limits of judge 1 on this job: audio was not transcribed (no speech-to-text tool), so caption wording and sync were
  judged from the picture; loudness measured at about -14 LUFS on all five; frames viewed at 4 fps and 240 px wide;
  figures in the Shorts (267 s, 208 s, 2.2X, 2.9X) not checked against the source material.
- Incidents: harness/blind.py got a one-line fix before the job A set was built (a crash on the «_duplicates» key;
  the old file was kept); it affects letter assignment only. The director did not see the key before
  both judgements were on file and did not judge.
- Not said: two runs per model, one repeated run, one guide by one author, one third-model judge that could not play
  video or hear the audio, one person who named a first choice only.

## Both jobs together (no new claim, only the two verdicts side by side)
- Quality by the rule: «tie» on the explainer (7.5 against 7.0) and «tie» on the Short (8.5 against 8.0).
- Finished: 8 of 8 valid runs, 4 of 4 per model; one Fable 5.2 run repeated for an instrument fault.
- Time: Opus 5.5 faster by non-overlapping ranges on both jobs: the explainer 6.4-9.9 against 12.5-16.7 minutes (closest
  runs 2.6 minutes apart), the Short 28.3-37.5 against 37.8-39.3 (closest runs 0.3 minutes apart).
- The person's first choice was an Opus 5.5 video on both jobs (b3, a3); the reviewer's top score went to a Fable 5.2
  video on both (b1 with 8, a5 with 10). The Short's 10 belongs to a5, which is both the repeated run and the copy the
  reviewer saw twice and recognised; without a5 the Short has no Fable top score to report.
- Source row for the spoken line «our own machine's load once stretched a run by over half an hour»: the void
  run a4 ended at 72.7 active minutes and its repeat a5, same model and job on a quiet host, at 37.8 (runs.csv rows a4 and
  a5): 34.9 minutes apart; a4's final check alone took 1,696 s. It compares a run with its repeat; no counterfactual run
  under the same load without the fault exists.
- Corrected 2026-11-17 after the verifier's recomputation: the range of
  the other runs' final checks, the key-open time, and three wordings that graded a difference the rule only counts.
