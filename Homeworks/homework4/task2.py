with open("dict.txt", "r") as file:
    dict = file.read()
dict = dict.split("\n")
adj, noun, verb = [], [], []
for word in dict:
    if word[-2:] == "yo":
        adj.append(word)
    elif word[-2:] == "ka":
        noun.append(word)
    else:
        verb.append(word)
comb_adj = 0
for i in range(len(adj)):
    count = 1
    for j in range(i + 1):
        count = count * (len(adj) - j)
    comb_adj += count
cool_num = comb_adj * len(noun) * len(verb)
print(cool_num)
