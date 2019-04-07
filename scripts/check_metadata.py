"""Check that all texts in `texts/` are mentioned in metadata csv files.

Exits with non-zero exit code if something is wrong.

"""

import os
import glob
import csv
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    csv_filenames = glob.glob(os.path.join(BASE_DIR, "*.csv"))
    csv_filenames = [fn for fn in csv_filenames if 'post-stratification' not in fn]
    filenames_mentioned = []
    for csv_filename in csv_filenames:
        with open(csv_filename, "r") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                filenames_mentioned.append(row["filename"])
    novel_filenames = tuple(map(os.path.basename, glob.glob(os.path.join(BASE_DIR, "texts", "*.html"))))
    unmentioned = set(novel_filenames) - set(filenames_mentioned)
    if unmentioned:
        message = """Filenames in repository but unmentioned in csv files:\n""" + "\n".join(unmentioned)
        print(message, file=sys.stderr)
        sys.exit(1)
    mentioned_but_absent = set(filenames_mentioned) - set(novel_filenames)
    if mentioned_but_absent:
        message = """Filenames mentioned in csv files but absent in repository:\n""" + "\n".join(mentioned_but_absent)
        print(message, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
