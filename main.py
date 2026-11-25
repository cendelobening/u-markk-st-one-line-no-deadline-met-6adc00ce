import os

LINE = "I delegated the deadline to Future Me, but Future Me just declared bankruptcy, so now I'm here answering for a man who no longer exists."

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod(path, 0o644)
