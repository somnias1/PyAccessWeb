import re
text = open('regex.txt')
val = 0
for line in text:
    line = line.rstrip()
    # Busca cualquier set de números
    valist = re.findall('[0-9]+', line)
    # findall() Debido a que findall retorna una lista, se va a cambiar
    for item in valist:
        # Se convierten los valores a entero y se suman
        val += int(item)

print(val)
