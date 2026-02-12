#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def shell(cmd, cwd=None, check=True, capture_output=False):
    return subprocess.run(
        cmd, shell=True, cwd=cwd, check=check, capture_output=capture_output
    )


def log(message):
    print(message, file=sys.stderr)


def err(message, exit_code=1):
    print(message, file=sys.stderr)
    sys.exit(1)


def run_python_version():
    cwd = Path() / "python"

    def check_interpreter():
        exists_check = shell("which python", check=False, capture_output=True)
        if exists_check.returncode > 0:
            err('Python interpreter not found. Please ensure "python" is in your PATH.')
        log(f"Python interpreter: {exists_check.stdout.decode('utf-8').strip()}")

    def check_version():
        version_check = shell(
            "python -c 'import sys; print(sys.version)'", capture_output=True
        )
        log(f"Python version: {version_check.stdout.decode('utf-8').strip()}")

    def run():
        shell("time python solve.py", cwd)

    check_interpreter()
    check_version()
    run()


def run_crystal_version():
    cwd = Path() / "crystal"
    out = (Path() / ".build" / "crystal_solve").absolute()

    def check_compiler():
        exists_check = shell("which crystal", check=False, capture_output=True)
        if exists_check.returncode > 0:
            print(
                'Crystal compiler not found. Please ensure "crystal" is in your PATH.',
                file=sys.stderr,
            )
            sys.exit(1)
        print(
            f"Crystal compiler: {exists_check.stdout.decode('utf-8').strip()}",
            file=sys.stderr,
        )

    def compile():
        source = (cwd / "solve.cr").absolute()
        if not out.exists() or source.stat().st_mtime > out.stat().st_mtime:
            shell(f"crystal build --release -o '{out}' '{source}'", cwd=cwd)
            print(f"Built executable: {out}", file=sys.stderr)
        else:
            print(f"Using cached executable: {out}")

    def run():
        shell(f"time {out}")

    check_compiler()
    compile()
    run()


def run_go_version():
    cwd = Path() / "go"
    out = (Path() / ".build" / "go_solve").absolute()

    def check_compiler():
        exists_check = shell("which go", check=False, capture_output=True)
        if exists_check.returncode > 0:
            err('Go compiler not found. Please ensure "go" is in your PATH.')
        log(f"Go compiler: {exists_check.stdout.decode('utf-8').strip()}")

    def compile():
        source = (cwd / "main.go").absolute()
        if not out.exists() or source.stat().st_mtime > out.stat().st_mtime:
            shell(f"go build -o '{out}' '{source}'", cwd=cwd)
            log(f"Built executable: {out}")
        else:
            log(f"Using cached executable: {out}")

    def run():
        shell(f"time {out}")

    check_compiler()
    compile()
    run()


def run_ruby_version():
    cwd = Path() / "ruby"

    def check_interpreter():
        exists_check = shell("which ruby", check=False, capture_output=True)
        if exists_check.returncode > 0:
            err('Ruby interpreter not found. Please ensure "ruby" is in your PATH.')
        log(f"Ruby interpreter: {exists_check.stdout.decode('utf-8').strip()}")

    def check_version():
        version_check = shell("ruby -e 'puts RUBY_VERSION'", capture_output=True)
        log(f"Ruby version: {version_check.stdout.decode('utf-8').strip()}")

    def run():
        shell("time ruby solve.rb", cwd)

    check_interpreter()
    check_version()
    run()


def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument(
        "-x",
        "--program",
        choices={"python", "crystal", "go", "ruby"},
        help="select a version to run",
    )
    parser.add_argument(
        "--remove-output",
        action="store_true",
        help="remove generated '.build' directory",
    )

    args = parser.parse_args()
    create_build_dir()
    if args.program == "python":
        run_python_version()
    elif args.program == "crystal":
        run_crystal_version()
    elif args.program == "go":
        run_go_version()
    elif args.program == "ruby":
        run_ruby_version()

    if args.remove_output:
        build = Path() / ".build"
        if build.exists():
            shutil.rmtree(build)


def create_build_dir():
    build = Path() / ".build"
    build.mkdir(exist_ok=True)
    gitignore = build / ".gitignore"
    if not gitignore.exists():
        with open(gitignore, mode="w") as f:
            f.writelines(["*", os.linesep])


if __name__ == "__main__":
    main()
