#!/usr/bin/python3
import subprocess
import sys

def grep(pattern, extensions, directory):
    extoption = ""
    if len(extensions) > 0:
        extensions = ["*." + ext for ext in extensions]
        extpattern = ",".join(extensions)
        extoption = f"--include=\"{extpattern}\""
   
    cmd = f'grep -R {pattern} {extoption} {directory}'
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    grep(sys.argv[1], sys.argv[2:], '.')
