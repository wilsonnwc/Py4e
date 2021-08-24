import urllib.request, urllib.parse, urllib.error
import json

# test link: http://py4e-data.dr-chuck.net/comments_42.json
# actual link:  http://py4e-data.dr-chuck.net/comments_1313956.json

url = input('Enter location: ')
print("Retrieving", url)

#lesson: have to open the url with urllib
data = urllib.request.urlopen(url).read().decode()
print("Retrieved:", len(data), "characters")

#lesson: convert url data into python from JSON
js = json.loads(data)

count_list = list()
#when counting the data in child, add ["child"] after js:
for item in js["comments"]:
    count_list.append(item['count'])

print("Count:", len(count_list))
print("Sum:", sum(count_list))
