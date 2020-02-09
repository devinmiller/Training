import sys
from collections import Counter
import load_dictionary

dict_file = list(load_dictionary.load('2of4brif.txt'))
# Ensure both "a" and "i" are included
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

ini_name = input('Enter a name: ')
ini_name = ''.join(ini_name.lower().split())

#letters = {k:v for (k,v) in Counter(ini_name)}
    
print(Counter(ini_name))