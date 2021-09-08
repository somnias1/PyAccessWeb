
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Encuentra los valores para cada posición
url = input('Enter URL: ')
Count = int(input('Enter count: '))
Position = int(input('Enter position: '))-1  # Corrección de vectores
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Busca los tags de enlace
tags = soup('a')

# Recorre la cantidad entregada
for i in range(Count):
    # El siguiente enlace a seguir está en la posición dada
    urlaux = tags[Position].get('href', None)
    # Qué nombre está siendo seguido
    print('Retrieving: ', tags[Position].contents[0])
    html = urllib.request.urlopen(urlaux).read()
    soup = BeautifulSoup(html, "html.parser")
    # Refresca los tags de enlace encontrados
    tags = soup('a')
