import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Recibe una URL, si no se entrega una, se usa una por defecto
url = input('Enter location: ')
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_200531.xml"
print('Retrieving', url)

xml = urllib.request.urlopen(url, context=ctx)
# Lee el XML
data = xml.read()
print('Retrieved:', len(data), 'characters')

tree = ET.fromstring(data)
# Encuentra la subsección del contador
counts = tree.findall('.//count')
print('Count:', len(counts))

accs = 0
# Extrae el texto y lo suma
for count in counts:
    accs += int(count.text)

print('Sum:', accs)
