import sys
from pathlib import Path

def main(needs, index):
    outpath = Path("output") / f"{needs}_{index}.txt"
    outpath.write_text(f"{needs}_{index}")

if __name__ == "__main__":
    main(*sys.argv[1:])
