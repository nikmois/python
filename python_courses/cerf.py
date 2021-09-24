import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sum = 0
url = 'http://py4e-data.dr-chuck.net/comments_432380.xml'
html = urllib.request.urlopen(url).read()
stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment/count')
print('User count:', len(lst))

for count in lst:
    sum = sum + int(count.text)


print('total:', sum)
