# Guide: how to work here

You are editing a video by writing an **edit file**: a text (YAML) file that a program, "the editor", turns into an
mp4 frame by frame on the CPU. Nobody clicks a timeline. You write the file, check it, look at a still or two,
render it, and deliver. This guide is all the help you get.

## 1. House rules (these bind every run)

- Your **job folder** is the folder this guide sits in. Work only inside it. Never read, list, write or delete
  anything outside it (other folders in the project are somebody else's work).
- `material/`, `brand/`, `GUIDE.md`, `BRIEF.md` and `bin/` are read-only. Write only in `work/` (your edit files,
  stills, scripts), `out/` (rendered videos) and `NOTES.md` (in the job folder). `logs/` is kept by the system.
- Run everything through **`bin/ed`** (section 3). Python runs only as `bin/ed py script.py`, which applies a memory
  cap. Do not call python, the editor or ffmpeg directly. The only exceptions are plain shell file tools (ls, cat,
  cp, mkdir).
- Renders go through `bin/ed render` only. The render runs on a shared machine and may wait for its turn: that wait
  is normal and is counted. Do not start a second render while one is running.
- Write your files (edit files, scripts, notes) with your file-writing tool, not with a shell here-document:
  a guard on this machine sometimes refuses shell commands that carry long pasted text.
- No network is needed or available. Do not install anything.
- The prompt gives you a time limit and a limit on the number of renders. Use renders to finish, and use `bin/ed
  frame` (a single still, much cheaper) to look at the picture while you work.

## 2. How the editor thinks

- **Times** in an edit file are seconds (`2.5s` or `2.5`), frames (`f60`) or beats (`b8`). Use seconds.
- The file has a few top-level settings (`fps`, `size: [w, h]`, `end`), then a list of **events**, each with a `t`
  (when it starts) and a `type`.
- Every moment of the video belongs to a **shot**. A shot starts with a `cut` event (a video file, a still image, or a
  flat colour: `color: "#0E0E0E"`) or a `card` event, and lasts until the next `cut`/`card`. Other events (type, numbers,
  captions, camera moves, light effects) sit on top of the shot that contains their `t`.
- A small "AI" tag is drawn by the editor on every frame (`mosca: true`). Leave it on; it is part of the channel's
  rules.
- Fonts and colours default to the channel's look (identity C, see `BRIEF.md` and `brand/`).

Two ways to get an edit file:

1. **A treatment** (best for footage with speech). You write a short `treatment.yaml`: which stretches of which take
   to keep, and which spoken phrases get which effect. `bin/ed treat` turns it into the full edit file, with
   captions, jump cuts that remove dead air, camera windows and a sound layer made by the editor. Captions and a
   9:16 crop from 16:9 footage come with it.
2. **Writing events by hand** (best for graphics without footage, or when you want full control). You write the
   events yourself. A treatment's output is also a normal edit file that you may edit by hand afterwards.

`bin/ed ref comp` prints the editor's full reference of events (long). `bin/ed ref treat` prints the treatment
reference. Read them when you need a key that is not below.

## 3. The commands

Paths given to `bin/ed` on the command line are relative to the job folder (or absolute). **Paths written inside a
file are different**: in a treatment they are relative to the treatment file (so from `work/t.yaml` the material is
`../material/...`); in a hand-written edit file they must be absolute (`bin/ed where` prints your job folder's
absolute path to put in front of `material/...`).

| command | what it does |
|---|---|
| `bin/ed ref comp` / `bin/ed ref treat` | the editor's own reference text |
| `bin/ed words-show material/words/take01.json` | a word file printed with times |
| `bin/ed words FILE OUT.json --language en` | recognise speech in any audio or video file, write word times (CPU, 1-3 minutes per file; the word files for the takes are already in `material/words/`) |
| `bin/ed treat work/t.yaml --check` | check a treatment, write nothing; prints every problem at once |
| `bin/ed treat work/t.yaml --out work/t.events.yaml` | write the edit file from a treatment |
| `bin/ed check work/e.yaml` | compile an edit file, print its shots and effects and every problem (exit 1 on a problem) and the layout lint's hits |
| `bin/ed lint work/e.yaml` | the layout lint alone; exit 1 on any hit |
| `bin/ed defaults work/e.yaml` | the production-defaults check alone; exit 1 on any hit |
| `bin/ed verify work/e.yaml` | check + lint + defaults; the three "own checks". A finished edit has all three `ok` |
| `bin/ed frame work/e.yaml N work/f.png` | draw frame number N as a PNG (first call is slow; view it with your image viewer) |
| `bin/ed render work/e.yaml out/name.mp4` | render the edit file to a video. Add `--frames 0:48` after the output name to render only up to frame 48, for a quick look (it counts as a render) |
| `bin/ed where` | print the absolute path of your job folder |
| `bin/ed probe out/name.mp4` | size, duration, streams of a video |
| `bin/ed py work/script.py` | run your own python (numpy, PyYAML, OpenCV available) |

The checks may wait several minutes for free memory on the shared machine ("waiting for RAM"): that is normal.

## 4. Writing an edit file by hand (events)

A complete small example. It makes 8 seconds of 1280x720 video from flat dark shots, a kinetic word, a data
panel with a number that counts up, and a flash. Copy it to `work/` and change it.

```yaml
version: 1
fps: 24
size: [1280, 720]
free_cuts: true            # shots start where you say, not on a music beat (always use this without music)
end: 8s                    # the length of the video
events:
  - {t: 0s,   type: cut, id: s1, color: "#0E0E0E"}
  - {t: 0.3s, type: kin, kind: slam, text: "FEWER STEPS", color: "#F4F4F1", cap: 70, dur: 1.8s}
  - {t: 3s,   type: cut, id: s2, color: "#0E0E0E"}
  - {t: 3.3s, type: panel, id: p1, x: 300, y: 200, w: 680, label: "BASE MODEL",
     figures: [{text: "600", sub: "SECONDS A CLIP", count: 18}], dur: 3s}
  - {t: 6.5s, type: flash, n: 2}
```

Event types you are likely to want (all keys optional unless shown; `bin/ed ref comp` has the rest):

- `cut` `{t, id, color | src, ss}`: a shot. `src` is a video or an image file; `ss` is the start second inside it.
- `kin` `{t, kind: slam|whisper|sliced|jump|marquee, text, cap, color, place, dur}`: kinetic type. `t` is the moment
  of impact. `cap` is the cap height in pixels at the piece's size. Big text must stay inside the title-safe area
  (the lint reports `leaves the title-safe area`).
- `titlecard` `{t, kicker, lines: [..], sub, dur, align, cap}`: a full-frame title card that builds in.
- `panel` `{t, id, x, y, w, label, figures: [{text, sub, count, ink, size}], dur}`: a light data panel with one or
  two big figures; `count` rolls a number up over that many frames. Inks: `k`, `cyan_ink`, `magenta_ink`.
- `kicker` `{t, lines: [..], band, sub, x, y, size, dur}`: one to four words straight on the picture, with an
  optional yellow marker band behind one word.
- `caption2` / `podcast`: word-by-word captions (see section 5).
- `punch`, `push`, `pan`, `kick` `{t, ...}`: camera moves on the current shot.
- `burn`, `flash`, `white`, `wash`, `insert`: light effects between shots. Not allowed to flicker more than three
  times a second.
- `grid` `{t, id, tiles: [{id, src, ss, rect: [x, y, w, h], label}]}`: several moving tiles on one dark card.

Rules the editor enforces (a violation shows up as a problem in `check`, or a hit in `lint`/`defaults`): text must
stay inside the title-safe area, two pieces of text must not overlap, a shot that does not change for too long is
refused unless `free_cuts: true`, an effect must not run outside the piece, and a source must be long enough for
the part you ask of it.

### Details that matter (found by whoever tried this before you)

- `x`, `y` of a `panel` or `kicker` are pixels of the frame (the top-left of the block; a kicker may add
  `anchor: center`, then `x` is its centre). A kicker without `x` and `y` crashes with a traceback that ends `needs x`.
- The ink of a `panel` and of a `kicker` is dark (#111). A `panel` has its own light plate; a `kicker` has no plate,
  so on a dark shot it is invisible. Use a panel, or `kin` text. `kin` text is dark by default too: on a dark shot
  give it `color: "#F4F4F1"` (or another light colour).
- `cap` is the cap height in pixels. Wide text must fit inside the title-safe area: 12 capital letters at about
  `cap: 120` fit at 1920 px wide; a longer line needs a smaller `cap` (the lint says `leaves the title-safe area`).
- An effect's span includes its entrance, a few frames before `t`, and its `dur` after it. Two texts whose spans
  touch are reported as overlapping (leave at least half a second), and nothing may run past `end` (the check says
  `run outside the piece`).
- With two or more titles in a piece, the defaults check (`T1`) asks that at least one of them is a special kind
  (`kin` with `kind: whisper`, `sliced`, `jump` or `marquee`), not only plain slams and kickers.
- `bin/ed check` and `verify` print one JSON line per event before the verdict; the verdict is at the end. Add
  `| grep -v '^{"what"'` to see only the problems.
- `bin/ed frame` takes a second or two; use it after every change of layout. `bin/ed render` is for the real thing.

## 5. Working from footage with speech (treatment)

Word times for every take are in `material/words/`. A treatment names a source video and its word file, then lists
the stretches kept (seconds of that source), in the order they play. Each stretch can have its own `src` and `words`.
Effects are placed by **phrase**: `at:` is words the speaker says inside that stretch.

```yaml
version: 1
piece: "short"
route: client
format: {size: [1080, 1920], fps: 24}        # vertical; 16:9 takes are cropped to 9:16 windows for you
source: {video: ../material/takes/take02.mp4, words: ../material/words/take02.json}      # relative to this file (work/t.yaml)
keep:
  - {id: hook,  from: 0.0, to: 7.0}                                                       # seconds of the source
  - {id: next,  src: ../material/takes/take06.mp4, words: ../material/words/take06.json, from: 0.0, to: 5.5}
look:                                          # the channel's look: brand fonts and colours (otherwise a neutral look is used)
  font: ../brand/anybody-latin-wdth-normal.woff2
  weight: 900
  case: upper
  ink: "#111111"
  plate: "#FBFBFA"
  accent: "#FFD400"
  band_ink: "#111111"
  fill: "#FBFBFA"
  outline: "#111111"
  outline_w: 0.10
  contrast: auto
  card: {ground: "#0E0E0E", ink: "#F4F4F1", accent: "#FFD400", muted: "#8E8E8A"}
captions: {size: 36, position: 0.8}          # size is relative to the frame; if a check says a word is too wide, lower it. position: share of the frame height
effects:
  - {keep: hook, at: "against her face", do: slam, text: "FACE", cap: 120, dur: 1.4}
```

Notes on treatments:
- `bin/ed treat work/t.yaml --check` first, until it prints OK. It refuses effects that overlap, too many slams per
  minute, words the speaker did not say, and so on, with the closest match.
- `do:` values: `slam`, `kicker`, `figure`, `title`, `chapter`, `panel`, `tag`, `qr`, `burn`, `flash`, `broll`
  (a still or video file in a slot, with `clip:`), `word`/`ring`/`marquee` (need a person matte; none here).
- A treatment can also carry `auto: {density: rich|normal|calm}` (the editor plans effects from the words) and
  `streamer: {preset: streamer_v5_3}` (a short-form preset: big captions, flashes, a hook header). Try
  `bin/ed ref treat` for every key.
- Captions are automatic. Do not write them by hand in a treatment.
- A treatment is for speech. To show a result clip (a `results/` file) in a shot of its own, use a `broll` effect with
  `clip:` (plus a `prompt:` of 30+ characters describing it, a `model:` label, and `dur` equal to the clip's length:
  the editor trims at most 1 s off a clip), or write the edit file's events by hand after `treat` has written it
  (`cut` events with `src` and `ss`). A phrase after `at:` must be words the speaker really says inside that stretch;
  the closest match is offered when it is not.
- `bin/ed treat` writes the edit file and turns the AI tag on. It reads the footage, so it can take a minute.
- The edit file that `treat` writes is plain text: you can open it, change it, and render it. After changes, run `bin/ed
  verify` again.

## 6. Checks, in plain words

`bin/ed verify FILE` runs three checks, each of which must end `ok`:
1. **check**: the file compiles; every source exists and is long enough; no rule above is broken.
2. **lint**: the layout: text over a face, text off the title-safe area, overlaps, a word repeated on screen,
   too little contrast.
3. **defaults**: the channel's production defaults (for example: a plain-only title card, or a graphic sitting on the
   presenter's face).

Each failing line says what and when (`t=14.04s`). Fix the file and run again.

## 7. Rendering and delivering

- `bin/ed render work/e.yaml out/short.mp4`. A full render of a minute of vertical video usually takes a few
  minutes plus any wait. The engine writes `out/short.mp4` and a `.inputs.json` and `.render_report.json` beside it.
- Check the result with `bin/ed probe out/short.mp4`: the size and duration must match the brief.
- Deliver: the final mp4 in `out/` (if several exist, the newest is the one that counts), its edit file(s) in `work/`,
  and `NOTES.md` as the prompt describes.
