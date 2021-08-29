from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')

#How many values and it's sum
Count=0
Suma=0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('Class:', tag.get('class', None))
    print('Contents:', tag.contents[0])
    #Add a new value found
    Count+=1
    #Add it to the acumulative
    Suma+=int(tag.contents[0])

#Print how many values were found and the sum
print(Count)
print(Suma)