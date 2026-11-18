"""voicecheck.py: does the render report's voice track cover the whole piece without gaps?"""
import json, os

JOB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
r = json.load(open(os.path.join(JOB, "out", "short.mp4.render_report.json")))
a = r["audio"]
print({k: v for k, v in a.items() if k != "voice_lines"})
end = 0.0
for v in a["voice_lines"]:
    gap = v["from_s"] - end
    if abs(gap) > 0.05:
        print("gap/overlap of %.3f s at %.3f" % (gap, end))
    end = v["from_s"] + v["dur_s"]
print("lines", len(a["voice_lines"]), "first from", a["voice_lines"][0]["from_s"], "last ends", round(end, 3))
