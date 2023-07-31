imp = input('Enter file name: ')
try:
    file = open(imp)
except:
    print ('enter a proper file name')
    exit()

mail = file.readlines()
for line in mail:
    if line.startswith ("X-DSPAM-Confidence"):
        spam_confidence = float(line.split(':')[1])
