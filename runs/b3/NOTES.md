# Job B: notes
- Made: `out/b-explainer.mp4`, 1920x1080, 24 fps, 20.00 s, h264, no sound. Edit file `work/e.yaml` (hand-written events); `work/bars.py` draws the shape plate `work/bars.mp4` that it uses.
- `bin/ed verify work/e.yaml`: check ok, lint ok (0 hits), defaults ok. 1 of 4 renders used.
- Five beats, all the text in order: light panel "WE TIMED ONE VIDEO CLIP / TWO WAYS / ON THE SAME GRAPHICS CARD" (0-4 s);
  a magenta bar grows while "600 SECONDS · 20 STEPS" counts up (4.4-8.5 s); a cyan bar on the same clock stops at 147/600 of the length while
  "147 SECONDS · 4-STEP SPEED LORA" counts up under the 600 (9.2-13.4 s); slam "4.1 TIMES" then sliced "AS FAST" (14-17 s);
  flash, then whisper "FEWER STEPS, FEWER SECONDS" with its yellow marker band (17.6-20 s).
- Decided: the bars are a time scale (both grow at one rate) so the 4.1x gap shows as length as well as numbers. They are drawn as a plate with no
  text, and the numbers sit in the editor's panel, so every word uses the brand fonts. Magenta = standard, cyan = speed LoRA.
- Tried and dropped: the `titlecard` event drew its kicker in yellow text (the brief allows yellow only as a band), so I replaced it with a panel.
  The whisper at cap 70 left the title-safe area, so I set it to cap 50. A top-level `sub:` on a panel is ignored, so it went inside the figure.
- Not done / caveats: no sound (optional in the brief). The slams use the editor's default cyan offset print (registration echo); I kept it as part of
  the house look, though a strict reading of "no shadows" could object. The whisper shows the closing line twice (band + large), which is how the effect works.
