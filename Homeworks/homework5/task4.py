import re
import sys


code = sys.stdin.readlines()
pattern = "(.+) = .+"

for n, line in enumerate(code):
    match = re.findall(pattern, line)
    for i in match:
        if re.findall("(\s*#)", i) == [] and re.findall("\[(\w+)\]", i) == []:
            lst = []
            match2 = re.findall("(\w+\.?\w*)", i)
            if len(match2) >1:
                for tupl in match2:
                    for word in tupl:
                        if word != '':
                            lst.append(word)
            else:
                lst.append(match2[0])

            print(n + 1, ' '.join(lst))