import sys

# print(sys.path)

import re

text = 'my umber is 66656556, el codigo es 211, lucky number is 23 '

result = re.findall('[0-9]+', text)

print(result)

import time

timestamp = time.time()
local = time.localtime()
result2 = time.asctime(local)
print(timestamp)
print(result2)

import collections 
#Imprime la frecuencia de cada numero
numbers = [1,2,4,5,6,1,2,4,55,9,1,3,5,5,6,2]
counter = collections.Counter(numbers)

print(counter)


