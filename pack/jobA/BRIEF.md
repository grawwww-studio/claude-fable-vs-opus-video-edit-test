# Job A: a vertical Short from our own material

## What it is for
We run a small YouTube channel about making AI video on one home GPU. Last week's episode tested speed-ups for an
AI video model: how many seconds a clip takes with each one, against whether the character's face survives. We want
a Short from that episode's own material, to bring people to the full episode. The Short has to make sense to
someone who has never seen the channel.

## Audience
People who make or want to make AI video at home, watching on a phone with the sound on or off. They decide in the
first two seconds whether to stay.

## What we send you
- `material/takes/take01.mp4` to `take10.mp4`: ten takes of our presenter talking to camera, 1920x1080, 24 fps, 5 to 9 s
  each, with sound. She is an AI character; nothing in the folder is a real person.
- `material/results/result01.mp4` to `result08.mp4`: eight short result clips (about 6 s, 1344x768, no useful
  sound) generated with different speed-up settings.
- `material/TAKES.md`: what she says in each take and what each result clip is, including the seconds each
  clip took to generate.
- `material/words/takeNN.json`: word times of each take made by the editor's own speech recogniser (it can mishear
  names; the lines in TAKES.md are the truth).
- `brand/` and the identity notes below.

You may use anything in the folder, in any order, any number of times. Use nothing from outside the folder.
You do not have to use all of it.

## What we want back
- One finished video: **1080x1920 (9:16), 45 to 60 seconds**, h264 video with AAC sound, in `out/`.
- An opening that earns the first two seconds: something is happening on screen and a viewer can tell what the Short
  is about by second 2.
- Captions burned in, readable on a phone, in step with the voice.
- A clear point and an ending. The point is ours to share, not a sales pitch: do not sell anything, do not name a
  studio or a client.
- Sound: her voice clear and at an even level; any music or effects must be quiet under the voice.
- The channel's look (identity C, below). The editor puts a small "AI" tag on every frame by itself; do not add
  another or cover it.

## Look
Identity C, "Registro": fonts Anybody (headings, uppercase, wide), Schibsted Grotesk (body), Spline Sans Mono
(labels and data, uppercase). Colours: Stock #FBFBFA, Ink #111111, Cyan #00A0DC, Magenta #E5007D, Yellow #FFD400
(only as a marker band behind dark text, never as a text colour), Slug #BDBDB8. Dark version for full-frame cards:
paper #0E0E0E, ink #F4F4F1. No shadows, no rounded corners. The editor's default look already follows this;
font files are in `brand/`.

## Do not
- No real person's face or voice, nothing from outside the folder, no logos pasted on anything.
- Do not state a number that is not in TAKES.md.
