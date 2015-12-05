from lxml import etree
import requests


url = "https://twitter.com/googlefacts"
data = requests.get(url).text

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

result = ''
for element in tree.iter("p"):
    if "class" in element.attrib:
            if element.attrib["class"] == "TweetTextSize TweetTextSize--26px js-tweet-text tweet-text" \
                    or \
                    element.attrib["class"] == "TweetTextSize TweetTextSize--16px js-tweet-text tweet-text":
                result += element.text + '\n'

with open("twitter.txt", "w") as out:
    out.write(result)
