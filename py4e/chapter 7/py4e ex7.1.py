input_file = input('enter file name: ')
try:
    pip = open (input_file)
except:
    print ('input a proper file name')  
    quit()
fil= pip.read()
lines = fil[:1000]
fil = lines.upper()
print (fil)