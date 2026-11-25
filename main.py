"""Write the roast entry to /output/entry.txt.

The entry text is fixed: one line, 100 characters, written exactly as
given, UTF-8, with no trailing newline. After writing, the file is read
back and checked byte for byte against the entry text; any mismatch
makes the program fail instead of silently shipping a wrong entry.
"""

import os
import sys

ENTRY = 'My agent calls every fix "a small change," which is how I know it hasn\'t opened the second file yet.'


def main():
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry length {len(ENTRY)} is outside 1-200", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("entry.txt does not match ENTRY exactly", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
