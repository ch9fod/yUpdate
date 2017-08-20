import requests
import feedparser

URL = "https://yts.ag/rss"

response = requests.get(URL)
with open('yts.xml', 'wb') as file:
    file.write(response.content)
d = feedparser.parse(r'yts.xml')
print(d)
