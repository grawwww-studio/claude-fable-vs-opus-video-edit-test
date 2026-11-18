# Job B notes

Made: `out/ep11-speed-lora-insert.mp4`, 1920x1080, 24 fps, 20.00 s, h264, no audio. It was rendered from `work/e.yaml`, which I wrote by hand. `bin/ed verify` reports check, lint and defaults all `ok`. I used 1 of the 4 renders.
Structure, all on dark identity-C cards:
- 0-3.8 s: title card "SAME GRAPHICS CARD / ONE CLIP / TIMED TWO WAYS".
- 3.8-7.8 s: light panel "STANDARD / 20 STEPS", with 600 SECONDS counting up in cyan.
- 7.8-11.6 s: panel "SPEED LORA / 4 STEPS", with 147 SECONDS counting up in magenta.
- 11.6-15 s: a bar chart at true scale (600 = 1500 px, 147 = 368 px), labelled "20 STEPS 600 S" and "4 STEPS 147 S".
- 15-17.6 s: a "4.1X AS FAST" slam with a camera kick.
- 17.6-20 s: a "FEWER STEPS, FEWER SECONDS" whisper.
Every number in the text appears on screen: 20, 600, 4, 147 and 4.1. No other number is used.
Decisions:
- The bars are two solid-colour PNGs that I made with `work/bars.py`, shown as `grid` tiles. They are shapes only, no photos.
- Slow pushes on the panel and bar shots keep the holds from looking frozen.
What did not work:
- `kin` with `place: top` crashed the editor, because place has to be a dict.
- A wide side-by-side panel overlapped the 147 panel's exit (lint L1), so I replaced it with the bars.
- The whisper at cap 64 left the title-safe area; it is at cap 48 now.
- `tile state: highlight` made no visible change, so I dropped it.
Not done:
- No sound. It was optional, and the editor's sound layer comes from `treat`, which needs speech footage, and `material/` is empty.
