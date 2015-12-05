import re
import requests

with open("links.txt", "r") as f:
    links = f.readlines()

pattern = "(\w+([._]\w+)*@\w+([._]\w+)*)"

text = ''
for link in links:
    html = requests.get(link).text
    text += html

found = re.findall(pattern, text)
result = []
for link in found:
    if link[0] not in result:
        result.append(link[0])

with open("email_addresses.txt", "w") as out:
    out.write("\n".join(result))
