import sys
import re


data = sys.stdin.read()
print(len(re.findall("[yY]ou", data)))