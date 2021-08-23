import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# http://py4e-data.dr-chuck.net/comments_42.xml

url = input('Enter location: ')
print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()
print("Retrieved:", len(data), "characters")
tree = ET.fromstring(data)
sum = 0
datacount = tree.findall('.//comment')
print("Count:", len(datacount))

for content in datacount:
    name = content.find('name').text
    count = content.find("count").text
    #print(name, count)
    sum = sum + int(count)

print("Sum:", sum)
print("Sum:", sum)
