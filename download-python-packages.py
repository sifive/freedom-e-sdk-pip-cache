#!/usr/bin/env python3

import sys
import subprocess
from itertools import product

if __name__ == "__main__":
    requirements = sys.argv[1]

    platforms = ["manylinux1_x86_64", "macosx_10_13_x86_64", "win32", "win_amd64"]
    versions = ["35", "36", "37"]

    tuples = product(platforms, versions)

    base_cmd = ["pip", "download", "-d", "pip-cache", "-r", requirements]

    subprocess.run(base_cmd + ["--platform", "any", "--no-deps"])

    for platform, version in tuples:
        subprocess.run(base_cmd + ["--platform", platform, "--python-version", version, "--only-binary=:all:"])

    print(list(tuples))

