import time

BASE_FILE = "base.m3u"
TOKEN_FILE = "token.txt"
OUTPUT_FILE = "playlist.m3u"

with open(TOKEN_FILE, "r", encoding="utf-8") as f:
    token = f.read().strip()

with open(BASE_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
for line in lines:
    line = line.strip()
    if line.startswith("http"):
        if "?" in line:
            line = line.split("?")[0]
        line = f"{line}?{token}"
    out.append(line)

header = f"#EXTM3U\n#Generated on {int(time.time())}\n\n"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(header + "\n".join(out))

print("Playlist updated successfully")
