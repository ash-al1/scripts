#! /usr/bin/python

"""
Given the current time, generate list of timestamps in available formats.
Useful in communication and security applications where logging is required.
"""

import sys
import time
import argparse

from datetime import datetime, timezone


# Offsets from UNIX
UNIX_OFFSET    = 0
APFS_OFFSET    = 0
FIREFOX_OFFSET = 0
COCOA_OFFSET   = 978307200
FAT_OFFSET     = 315532800
HFS_OFFSET     = 2082844800
WEBKIT_OFFSET  = 11644473600000000
NTFS_OFFSET    = 116444736000000000


def return_timestamps():
    """
    Generates and stores dict of all listed formats available.
    """
    base_unix_time = time.time()
    date_time = datetime.fromtimestamp(base_unix_time, timezone.utc)

    timestamps = {
        'Unix' : base_unix_time,
        'HFS+' : base_unix_time - HFS_OFFSET,
        'Cocoa' : base_unix_time + COCOA_OFFSET,
        'WebKit' : (base_unix_time * 1e6) + WEBKIT_OFFSET,
        'NTFS' : (base_unix_time * 1e6) + NTFS_OFFSET,
        'FAT' : base_unix_time + FAT_OFFSET,
        'APFS' : base_unix_time * 1e9,
        'FireFox' : base_unix_time * 1e6,
        'ISO8601_Basic' : date_time.strftime('%Y%m%dT%H%M%SZ'),
        'ISO8601_Extended' : date_time.isoformat() + 'Z',
        'RFC3339' : date_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+00:00',
        'RFC2822' : date_time.strftime('%a, %d %b %Y %H:%M:%S +0000'),
        'CommonLog' : date_time.strftime('%d/%b/%Y:%H:%M:%S +0000'),
    }

    return timestamps

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--formats", type=str,
                        help="selected formats", required=False)
    parser.add_argument("-a", "--all", action="store_true",
                        help="spit out all timestamps")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="suppress banner")
    parser.add_argument("-l", "--list", action="store_true",
                        help="list available formats")
    args = parser.parse_args()

    # require a flag
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⡞⡀⣤⣤⣴⠀⠀⢳⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⢻⣿⡇⠀⢸⣿⠿⣿⡇⠀⠀⠸⣿⣧⡘⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀description: generate timestamps
⠀⠀⠀⠀⠀⠀⠀⡸⣫⣿⡛⢛⡸⣿⡇⠀⠈⢿⣧⡝⠟⠀⠀⢸⣿⣿⠙⠻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀author: ash
⠀⠀⠀⠀⠀⠀⠀⡾⢿⣿⣿⡻⣴⣸⣿⣆⣠⣶⣿⣿⣷⣄⣰⣿⢛⣷⣴⣷⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠴⠋⣽⠋⡸⢱⣯⡿⣿⠏⣡⣿⣽⡏⠹⣿⣿⣿⡎⢣⠙⢿⡙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠁⠘⠏⠁⠁⠸⣶⣿⡿⢿⡄⠈⠀⠁⠃⠈⠂⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    if not args.quiet:
        print(banner)

    # list of all generated keys
    timestamps = return_timestamps()
    max_key_length = max(len(key) for key in timestamps.keys())
    print("")

    # provide a list of all available timestamp formats
    if args.list: 
        list_of_names = "Formats available:"
        for name, _ in timestamps.items():
            list_of_names = list_of_names + " " + name
        print(list_of_names)

    # return all timestamps
    elif args.all:
        for name, val in timestamps.items():
            print(f"{name:<{max_key_length}} : {val}")

    # return formats selected by user
    elif args.formats:
        formats_listed = args.formats.split(",")
        formats_listed = [key.lower() for key in formats_listed]
        for name, val in timestamps.items():
            if name.lower() in formats_listed:
                print(f"{name} : {val}")


if __name__ == "__main__":
    main()
