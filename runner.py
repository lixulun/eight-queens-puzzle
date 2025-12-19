#!/usr/bin/env python3

import argparse
import subprocess


def run_python_version():
    subprocess.run("python3 solve.py".split())


def run_crystal_version():
    subprocess.run("crystal solve.cr".split())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-x",
        "--program",
        required=True,
        choices={"python", "crystal"},
        help="指定执行哪个版本",
    )

    args = parser.parse_args()
    if args.program == "python":
        run_python_version()
    elif args.program == "crystal":
        run_crystal_version()


if __name__ == "__main__":
    main()
