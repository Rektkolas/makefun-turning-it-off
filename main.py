"""Make.fun entry: Have You Tried Turning It Off?.

Writes one line to /output/entry.txt (ENTRY_OUTPUT override for local
testing).
"""
import os

LINE = "Have you tried turning it off and on again? It's either that or I transfer you to Dave, and Dave turned himself off in 2019."


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        fallback = os.path.join(os.getcwd(), "output", "entry.txt")
        os.makedirs(os.path.dirname(fallback), exist_ok=True)
        with open(fallback, "w", encoding="utf-8") as f:
            f.write(LINE)


if __name__ == "__main__":
    main()
