num = 0
total = 0.0
max = None
min = None
while True:
    scr = input ("input number:" )
    if scr == "done":
        break
    try: 
        score = float (scr)
        num = num + 1
        total = score + total
    except:
        print ("input a valid number....")
        continue
    if max is None or max > score: 
        max = score
    if min is None or min < score: 
        min = score
print (num, ",", total, ",", max,",", min)    
