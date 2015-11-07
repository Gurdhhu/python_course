with open('yazkora.txt', 'r') as f:
    text = f.read().split('.')
    for i in range(len(text)):
        formatted_string = []
        for k in text[i].split(' '):
            if k != '':
                for j in k.split('\n'):
                    if j != '':
                        formatted_string.append(j)
        text[i] = formatted_string
    output = ''
    for i in text:
        words = []
        for j in i:
            if j[-2:] == 'yo':
                words.append(j)
        output += ' '.join(words) + '\n'
with open('answer.txt', 'w') as out:
    out.write(output)