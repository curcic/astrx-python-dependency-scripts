import re
import sys

if len(sys.argv) != 3:
    exit(1)


def validate_filename(filename):
    if not re.match(r"^[\w.]+$", filename):
        raise ValueError("Invalid characters in file name")
    if ".." in filename:
        raise ValueError("Invalid file name")


validate_filename(sys.argv[1])

with open(sys.argv[1], "w") as f:
    f.write(sys.argv[2])
