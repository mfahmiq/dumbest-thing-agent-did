"""Write one line about the dumbest thing my agent did today.

The line: my agent spent forty minutes "fixing" a bug by rewriting the
only file that worked, then deleted the original and asked me to review
its improvement. It must stay a single line of 1-200 characters, so this
module asserts that bound before writing.
"""

import os

LINE = (
    "My agent spent 40 minutes 'fixing' a bug by rewriting the only file "
    "that worked, then deleted the original and asked me to review its "
    "improvement."
)

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
# The line is 146 characters.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
