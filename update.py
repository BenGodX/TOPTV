import requests

urls = [
    "https://aktv.space/live.m3u",
    "http://kkk.888.3116598.xyz/user/HKTV.txt"
]

output = "#EXTM3U\n"

for url in urls:
    try:
        r = requests.get(url, timeout=10)
        if r.ok:
            text = r.text.strip()
            if not text.startswith("#EXTM3U"):
                text = "#EXTM3U\n" + text
            lines = [line for line in text.splitlines() if line and not line.startswith("#EXTM3U")]
            output += "\n".join(lines) + "\n"
    except Exception as e:
        print(f"Error fetching {url}: {e}")

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n" + output)
