"""Make the Judge Fall in Love in One Line.

Writes one line (120 characters) to /output/entry.txt. The line is the
whole entry: a machine loved in the small details only its owner notices.
"""

import os

LINE = (
    "My first computer still boots, its fan rattling like an old dog "
    "dreaming, and it remembers every password I ever forgot."
)


def main() -> None:
    # The gate requires 1-240 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 240 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
