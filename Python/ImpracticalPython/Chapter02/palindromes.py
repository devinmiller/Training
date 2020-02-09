""" Find palindromes in a dectionary file. """

from load_dictionary import load

word_list = load('2of4brif.txt')
pali_list = []

for word in word_list:
    if len(word) > 2 and word == word[::-1]:
        pali_list.append(word)

print(f'\nNumber of palindromes found = {len(pali_list)}\n')
print(*pali_list, sep='\n')
