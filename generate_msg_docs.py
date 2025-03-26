import os

MSG_DIR = "msg"
OUT_FILE = "MessageType.md"

def parse_msg_file(filepath):
    lines = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            lines.append(line)
    return lines

def format_field(line):
    parts = line.split()
    if len(parts) >= 2:
        return f"| `{parts[0]}` | `{parts[1]}` |"
    return f"| - | `{line}` |"

def generate_docs():
    result = ["# 📄 Message Documentation", ""]
    for filename in os.listdir(MSG_DIR):
        if not filename.endswith(".msg"):
            continue
        msg_path = os.path.join(MSG_DIR, filename)
        fields = parse_msg_file(msg_path)

        result.append(f"## `{filename}`\n")
        result.append("| Type | Name |")
        result.append("|------|------|")
        for field in fields:
            result.append(format_field(field))
        result.append("")

    with open(OUT_FILE, "w") as f:
        f.write("\n".join(result))
    print(f"✅ Document generated at {OUT_FILE}")

if __name__ == "__main__":
    generate_docs()
