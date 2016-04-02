#!/usr/bin/python3.4
import argparse
import os
import subprocess


parser = argparse.ArgumentParser(description="This script helps to reduce "
                                             "the size of your images")
parser.add_argument("percent",
                    type=int,
                    help="to what percent the image should be reduced")
parser.add_argument("path",
                    type=str,
                    help="image file or directory to process images")
parser.add_argument("newpath",
                    type=str,
                    nargs="?",
                    help="path to output file, only if input is a file")

args = parser.parse_args()
percent = str(args.percent) + "%"
path = args.path
newpath = args.newpath

if not os.path.exists(path):
    print("File or directory does not exist!")
elif os.path.isfile(path):
    if newpath is None:
        command = ["convert", path, "-resize", percent, path]
        subprocess.call(command)
    else:
        command = ["convert", path, "-resize", percent, newpath]
        subprocess.call(command)
else:
    file_names = []
    for desc in os.walk(path):
        prefix, subdir, files = desc
        files_with_prefix = [prefix + "/" + x for x in files
                             if x.endswith(".jpg") or x.endswith(".png")]
        file_names.extend(files_with_prefix)

    for file in file_names:
        command = ["convert", file, "-resize", percent, file]
        subprocess.call(command)

    print(" ".join([str(len(file_names)), "files converted"]))
