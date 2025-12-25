#!/usr/bin/env python3

import argparse
import subprocess


def run_python_version():
    subprocess.run("python3 --version".split())
    subprocess.run("python3 solve.py".split())


def run_crystal_version():
    subprocess.run("crystal -v".split())
    subprocess.run("crystal solve.cr".split())


def run_go_version():
    subprocess.run("go version".split())
    subprocess.run("cd go && go run main.go", shell=True)


def run_ruby_version():
    subprocess.run("ruby -v".split())
    subprocess.run("cd ruby && ruby solve.rb", shell=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-x",
        "--program",
        required=True,
        choices={"python", "crystal", "go", "ruby"},
        help="指定执行哪个版本",
    )

    args = parser.parse_args()
    if args.program == "python":
        run_python_version()
    elif args.program == "crystal":
        run_crystal_version()
    elif args.program == "go":
        run_go_version()
    elif args.program == "ruby":
        run_ruby_version()


if __name__ == "__main__":
    main()
