import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

result_url_list = list()
url = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_input = input('Enter URL: ')
url.append(url_input)
# sample: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# actual: http://py4e-data.dr-chuck.net/known_by_Chidera.html
position = input('Enter position: ')
position = int(position) - 1
count = input('Enter count: ')
count = int(count)


while count >= 0:
    result_url_list[:] = []  #remarks: necessary to clear the list for next while interation!
    url_to_do = url.pop(0)

    html = urllib.request.urlopen(url_to_do, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        # Look at the parts of a tag
        x = tag.get('href', None)
        result_url_list.append(x)

    #print("result url:", result_url_list[position])
    url.append(result_url_list[position])
    #print("url:", url)
    #print("url type:", type(url))
    print("Retrieving:", url_to_do)

    count = count - 1
#    print("remaining count", count)
