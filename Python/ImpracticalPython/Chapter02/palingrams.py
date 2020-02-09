"""Find all word-pair palingrams in a dictionary file"""
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')
word_list = set(word_list)

# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams"""
    palingram_list = []
    
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 2:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    palingram_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    palingram_list.append((rev_word[:end-i], word))
    return palingram_list

palingrams = find_palingrams()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print(f'Number of palingrams = {len(palingrams_sorted)}')

for first, second in palingrams_sorted:
    print(f'{first} {second}')

exit()