things = input()
number = int(input())
vocab = {"ложка": ("ложка", "ложки", "ложек"), "утюг": ("утюг", "утюга", "утюгов"), "чайник": ("чайник", "чайника", "чайников"), "гармошка": ("гармошка", "гармошки", "гармошек")}
wordlist = []
wordlist.extend(vocab[things])
def plural(number, words):
    if 10 < number % 100 < 20:
        return words[2]
    elif number % 10 == 1:
        return words[0]
    elif 1 < number % 10 < 5:
        return words[1]
    else:
        return words[2]
print(number, plural(number, wordlist))
