import urllib.request, urllib.parse, urllib.error
import json

sum = 0
lst = []
url = input("Enter URL")
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

info = json.loads(data)
comments = info['comments']
for item in comments:
    lst.append(item['count'])

for de in lst:
    sum = sum + de
print(sum)
