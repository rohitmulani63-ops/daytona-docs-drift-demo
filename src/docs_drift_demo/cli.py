from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Print a Daytona docs-drift demo status line.")
    parser.add_argument("--status", action="store_true", help="Show the demo status output.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.status:
        print("Daytona docs-drift demo: ready")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
