with open("dict.txt", "r") as file:
    dict = file.read()
dict = dict.split("\n")
adj, noun, verb = 0, 0, 0
for word in dict:
    if word[-2:] == "yo":
        adj += 1
    elif word[-2:] == "ka":
        noun += 1
    else:
        verb += 1
comb_adj = 0
for i in range(adj):
    count = 1
    for j in range(i + 1):
        count = count * (adj - j)
    comb_adj += count
cool_num = comb_adj * noun * verb
print(cool_num)
