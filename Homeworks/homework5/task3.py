import re
import sys


code = sys.stdin.readlines()

for n, line in enumerate(code):
    found = re.findall('(\w+) = .+', line)
    if len(found) != 0:
        print(n + 1, found[0])