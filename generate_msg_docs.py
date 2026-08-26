import os

MSG_DIR = "msg"
OUT_FILE = "MessageType.md"

def parse_msg_file(filepath):
    constants = []
    fields = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            # a constant is "<type> <NAME> = <value>"; the "=" never appears
            # in the type token except as a bounded-array marker ("[<=N]")
            if "=" in line.split(None, 1)[-1]:
                constants.append(line)
            else:
                fields.append(line)
    return constants, fields

def format_field(line):
    parts = line.split()
    if len(parts) >= 2:
        return f"| `{parts[0]}` | `{parts[1]}` |"
    return f"| - | `{line}` |"

def format_constant(line):
    type_name, rest = line.split(None, 1)
    name, value = rest.split("=", 1)
    return f"| `{type_name}` | `{name.strip()}` | `{value.strip()}` |"

def generate_docs():
    result = ["# 📄 Message Documentation", ""]
    for filename in sorted(os.listdir(MSG_DIR)):
        if not filename.endswith(".msg"):
            continue
        msg_path = os.path.join(MSG_DIR, filename)
        constants, fields = parse_msg_file(msg_path)

        result.append(f"## `{filename}`\n")
        if constants:
            result.append("| Type | Constant | Value |")
            result.append("|------|----------|-------|")
            for constant in constants:
                result.append(format_constant(constant))
            result.append("")
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
