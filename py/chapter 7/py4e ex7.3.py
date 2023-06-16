imp = input("input file name: ")
if imp == ("na na boo boo"):
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
try:
    file = open(imp)    
except:
    print ("enter proper file name...")