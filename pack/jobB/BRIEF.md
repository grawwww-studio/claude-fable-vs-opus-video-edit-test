# Job B: a 20-second motion-graphics explainer from one paragraph

## What it is for
A short animated insert for the same channel's next episode: it explains one measured result in text and
numbers, no footage and no presenter. It plays full-screen between talking sections, so it has to read in a
glance and look like it belongs to the channel.

## The text (say all of it, in this order; every number must appear on screen)
> We timed one video clip two ways on the same graphics card. With the standard 20 steps it took 600 seconds.
> With a 4-step speed LoRA it took 147 seconds. That is 4.1 times as fast. Fewer steps, fewer seconds.

## What we want back
- One finished video: **1920x1080 (16:9), 24 fps, 18 to 22 seconds**, h264, in `out/`.
- Motion graphics only: type, numbers, shapes, colour. No photos, no footage, no people.
- The two timings and the 4.1 ratio are the heroes: a viewer who sees it with the sound off must still get "600 s
  against 147 s, 4.1 times as fast".
- Sound is optional. If you add any, it must be quiet and from the editor's own sound layer. No voice-over is
  supplied, and none is needed: the text carries it.
- The channel's look (identity C, below). The editor puts a small "AI" tag on every frame by itself.

## Look
Identity C, "Registro": Anybody (headings, uppercase, wide), Spline Sans Mono (labels and data, uppercase).
Full-frame cards are dark: paper #0E0E0E, ink #F4F4F1, cyan #12A9E6, magenta #FF2D92, yellow #FFD400 (only as a
marker band behind #111 text, never as a text colour), slug #8E8E8A. No shadows, no rounded corners. The editor's
default look already follows this; font files are in `brand/`.

## Do not
- Nothing from outside the folder; no logos; no names of studios or clients; no number that is not in the text above.
