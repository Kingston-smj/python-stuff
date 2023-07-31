str = 'X-DSPAM-Confidence:0.8475'
col = str.find(':')
print (col)
last = str.find('5')
print (last)
flt = str [col+1:last+1]
num = float(flt)
print (num)