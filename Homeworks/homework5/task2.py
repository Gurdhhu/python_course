import sys
import re


data = sys.stdin.read()
lines = data.split("\n")
for i in lines:
    if len(re.findall("(1{3,11}|2{3,11}|3{3,11}|4{3,11}|5{3,11}|6{3,11}|7{3,11}|8{3,11}|9{3,11}|0{3,11})", i)) != 0:
        print(i)