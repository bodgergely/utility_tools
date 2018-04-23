#!/usr/bin/python3
import subprocess
import sys

def grep(pattern, extensions, directory):
    includes = ""
    if extensions:
        inc = "--include="
        includes = " ".join([inc + "*." + ext for ext in extensions])
   
    cmd = f'grep -R {pattern} {includes} {directory}'
    print(cmd)
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    extensions = []
    if len(sys.argv) > 2:
        extensions = sys.argv[2].split(',')
    grep(sys.argv[1], extensions, '.')
