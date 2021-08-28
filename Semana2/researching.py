import re
text = open('regex.txt')
val = 0
for line in text:
    line = line.rstrip()
    #Will search for any set of numbers
    valist = re.findall('[0-9]+', line)
    #findall() returns a list, let's change it
    for item in valist:
        #Every item in the list is a number, convert it to an int, then add
        val+=int(item)

print(val)