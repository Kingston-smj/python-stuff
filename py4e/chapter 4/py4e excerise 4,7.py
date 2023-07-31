def computegrade():
    x = float(score) 
    if 0.9<=x<=1:
        x='A'
    elif 0.8<=x<=0.89:
        x='B'
    elif 0.7<=x<=0.79:
        x='c'
    elif 0.6<=x<=0.69:
        x='D'
    elif x<=0.6:
        x='F'
    else:
        x= 'input number between 1 and 0'
    return x
score = input('score: ')
grade = computegrade()
print ('grade:', grade)