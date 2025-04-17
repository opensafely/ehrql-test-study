import csv
from pathlib import Path

import pyarrow.feather as feather


def main():
    input_files = Path("output").glob("dataset_*.arrow")
    counts = {}

    with open("output/count_by_year.csv", "wt") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["year", "total_prt_or_mal", "total_ace_or_arb"])
        for input_file in input_files:
            year = input_file.stem.split("_")[-1]
            df = feather.read_feather(input_file)
            writer.writerow([year, sum(df.prt_or_mal), sum(df.ace_or_arb)])

if __name__ == "__main__":
    main()
