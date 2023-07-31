count = 5
while True:
    imp = input("input file name: ")
    count = count -1
    if count < 1:
            quit()
    if imp == ("na na boo boo"):
        print("NA NA BOO BOO TO YOU - You have been punk'd!")    
    try:
        file = open(imp)    
    except:
        print ("enter proper file name...", ',', 'you have', count, 'tries remaining' )