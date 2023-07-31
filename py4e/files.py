fhand = open('mbox.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        line = line.rstrip()
        print(line)
        count = count + 1
        if count == 5:
            quit() 