#!/usr/bin/env python3

import argparse
import subprocess


def run_python_version():
    subprocess.run("python3 solve.py".split())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-x",
        "--program",
        required=True,
        choices={"python"},
        help="指定执行哪个版本",
    )

    args = parser.parse_args()
    if args.program == "python":
        run_python_version()


if __name__ == "__main__":
    main()
