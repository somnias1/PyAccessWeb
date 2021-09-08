import json
import ssl
import urllib.request
import urllib.parse
import urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter JSON URL: ')
print('Retrieving', url)

info = urllib.request.urlopen(url, context=ctx)
data = info.read().decode()
js = json.loads(data)
print('Retrieved', len(data), 'characters')
counter = 0

for item in js['comments']:
    print('Name:', item['name'])
    print('Count:', item['count'])
    counter += item['count']

print('Final count: ', counter)
