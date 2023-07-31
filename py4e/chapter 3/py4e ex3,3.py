score = input('score: ')
try:
    x = float(score) 
    if 0.9<=x<=1:
        print ('A')
    elif 0.8<=x<=0.89:
        print ('B')
    elif 0.7<=x<=0.79:
        print ('c')
    elif 0.6<=x<=0.69:
        print ('D')
    elif x<=0.6:
        print ('F')
    else:
        print ('input number between 1 and 0')
except:
    print ('please input figures')