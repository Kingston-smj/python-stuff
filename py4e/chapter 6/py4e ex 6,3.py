def enumarate(word,letter):
    appears = 0
    for letter in word:
        if letter == l:
            appears = appears + 1
    return appears
w = input ('type word:')
l = input ('type letter: ')
count = enumarate(w,l)
print (count)