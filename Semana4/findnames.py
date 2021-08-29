
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Finds values for the first iteration
url = input('Enter URL: ')
Count = int(input('Enter count: '))
Position = int(input('Enter position: '))-1 #Arrays start at 0, needs the adaptation
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

#Counts anchors followed
for i in range(Count):
    #The new url is the one at the Position
    urlaux = tags[Position].get('href', None)
    #Which name is being followed
    print('Retrieving: ', tags[Position].contents[0])
    html = urllib.request.urlopen(urlaux).read()
    soup = BeautifulSoup(html,"html.parser")
    #Changes the tag list for the next iteration
    tags = soup('a')
