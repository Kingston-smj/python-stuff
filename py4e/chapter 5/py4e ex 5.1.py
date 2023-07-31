num = 0
total = 0.0
max = None
min = None
while True:
    scr = input ('enter a number:' )
    if scr == 'done':
        break
    try:
        score = float(scr)
    except:
        print ('invalid input')
        continue
    num = num + 1
    total = score + total
    if max is None or max < score:
        max = score
    if min is None or min > score:
        min = score
print (num,',' , total,',', 'average:',total/num)
