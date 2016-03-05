out = []
classlib = {A: "A", B: "B", C: "C"}
for i in (A, B, C):
    if issubclass(D, i):
        out.append(classlib[i])

print(" ".join(out))
