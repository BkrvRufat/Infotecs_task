import re
import sys
from colorama import Fore

timestamp_format = 'DD-MM-YYYY HH:MM:SS'


# Convert timestamp to regex.
def gen_regex(date_format):
    symbols = 'YMDHS'
    for s in symbols:
        date_format = date_format.replace(s, r'\d')
    return date_format


# Find differences between files.
def diff_logs(lines1, lines2, ignore_case=True, ignore_patterns=None):
    ignore_patterns = ignore_patterns or []
    error_count = 0

    line_num = 0

    for line1, line2 in zip(lines1, lines2):
        line_num += 1

        if ignore_case:
            line1 = line1.lower()
            line2 = line2.lower()

        # If same lines of files are completly same then continue
        if line1 == line2:
            continue

        line1norm = line1
        line2norm = line2

        # Split different lines, for checking by date and path patterns
        for p in ignore_patterns:
            line1norm = ''.join(re.split(p, line1norm))
            line2norm = ''.join(re.split(p, line2norm))

        if line1norm == line2norm:
            continue

        error_count += 1
        print(Fore.CYAN  + f'\nDIFF LINE:{line_num}\n{Fore.GREEN}"{line1}"\n{Fore.BLUE}vs\n{Fore.RED}"{line2}"\n')

    # If lines counts are different in files, the script will calculate it as the difference
    error_count += abs(len(lines1) - len(lines2))
    return error_count

#
def main():

    # Make script parametrized
    try:
        file1, file2 = sys.argv[1:3]
    except:
        print("Invalid usage. Syntax: python3 diff.py /path/to/build1.log /path/to/build2.log")
        exit(1)

    with open(file1) as f:
        lines1 = [line.rstrip() for line in f.readlines()]
    with open(file2) as f:
        lines2 = [line.rstrip() for line in f.readlines()]

    # Pattern lists, that will ignore by the script in compare process(date and path)
    patterns = [
        # ignore date times
        gen_regex(timestamp_format),

        # ignore zlib paths
        r'zlib/[\d.]+',

        # ignore zlib paths for windows
        r'zlib\\[\d.]+',
        # ignore zlib version
        r'zlib version: [\d.]+',
        r'found zlib: [\d.]+',
        r'found version "[\d.]+"',
    ]

    error_count = diff_logs(lines1, lines2, ignore_patterns=patterns)

    if error_count == 0:
        print("Files are different only by date and path")
    else:
        print(f"SUMMARY: {error_count} lines are different")


if __name__ == '__main__':
    main()