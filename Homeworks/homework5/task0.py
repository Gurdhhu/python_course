import re
import sys


data = sys.stdin.read()
print(len(re.findall("you", data)))