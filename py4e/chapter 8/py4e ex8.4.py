file = open('romeo.txt')
fil = file.read ()
words = file.split()
wds = list()
for w in wds:
    if w not in wds:
        wds.append(w)
print (wds)

file = open('romeo.txt')
text = file.read()
words = text.split()
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(unique_words)
