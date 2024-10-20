import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(
        prog="dir-audit",
        description="Audit directory tree structure",
    )

    parser.add_argument("-v", "--version", action="store_true", default=False, help="Get dir-audit version")

    subparsers = parser.add_subparsers(
        dest="command", help="Audit command"
    )

    parser_make = subparsers.add_parser("make", help="Make directory tree")
    parser_check = subparsers.add_parser("check", help="Check directory tree")

    parser_make.add_argument("directory", choices=["handover"], help="Directory type")
    parser_make.add_argument("path", help="Directory destination")

    parser_check.add_argument("path", help="Directory path")
    parser_check.add_argument("-c", "--contains", help="List files and directories that contain given substring")
    parser_check.add_argument("-e", "--empty", action="store_true", default=False, help="Check if directory is empty")
    parser_check.add_argument("-f", "--full", action="store_true", default=False, help="Print full directory tree")

    args = parser.parse_args()

    if not args.version and not args.command:
        parser.print_help()
        sys.exit(0)

    return args

