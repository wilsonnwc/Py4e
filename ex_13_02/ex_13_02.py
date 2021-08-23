from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
numlist = list()

# sample: http://py4e-data.dr-chuck.net/comments_42.html
# actual: http://py4e-data.dr-chuck.net/comments_1313953.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    x = re.findall('[0-9]+', str(tag))
    numlist = numlist + x

numlist = [int(i) for i in numlist]
print(sum(numlist))
