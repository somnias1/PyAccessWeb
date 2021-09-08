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

# Extrae los datos que tengan el tag de span
tags = soup('span')

Count = 0
Suma = 0
for tag in tags:
    # Busca los componentes de los tags
    print('TAG:', tag)
    print('Class:', tag.get('class', None))
    print('Contents:', tag.contents[0])
    # Suma uno al contador por cada span encontrado
    Count += 1
    # Lo suma al acumulado
    Suma += int(tag.contents[0])

# Cuantos tags fueron encontrados y su suma
print(Count)
print(Suma)
