#!/usr/bin/python3.4
import argparse
import os
import shutil
import subprocess
import pwd

parser = argparse.ArgumentParser(description="Store and Diff script remembers "
                                             "the input file or directory content "
                                             "and then shows any changes "
                                             "introduced in it.")
parser.add_argument("function",
                    type=str,
                    choices=["store", "diff"],
                    help="choose the function: "
                         "store - to remember file or directory content, "
                         "diff - to display changes "
                         "between the current and stored "
                         "file or directory versions")
parser.add_argument("path",
                    type=str,
                    help="file or directory to store or check for changes")

args = parser.parse_args()
function = args.function
path = args.path


if function == "store":
    saddir = pwd.getpwuid(os.getuid()).pw_dir + "/.sad"
    if not os.path.exists(saddir):
        os.mkdir(saddir)
    name = "/" + path.split("/")[-1]
    if os.path.isfile(path):
        shutil.copy(path, saddir)
    elif os.path.isdir(path):
        shutil.copytree(path, saddir + name)
    else:
        print("The input is strange")

else:
    saddir = pwd.getpwuid(os.getuid()).pw_dir + "/.sad"
    name = "/" + path.split("/")[-1]
    if os.path.isfile(path):
        subprocess.Popen(["diff", path, saddir + name])
    elif os.path.isdir(path):
        subprocess.Popen(["diff", path, saddir + name, "-r"])
    else:
        print("The input is strange")