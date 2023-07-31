imp = input('Enter file name: ')
try:
    file = open(imp)
except:
    print('Enter a proper file name')
    quit()

mail = file.readlines()
count = 0
total_spam_confidence = 0

for line in mail:
    if line.startswith("X-DSPAM-Confidence:"):
        # Extract the spam confidence value from the line
        spam_confidence = float(line.split(':')[1])
        count = count + 1
        total_spam_confidence = total_spam_confidence + spam_confidence

file.close()

if count > 0:
    average_spam_confidence = total_spam_confidence / count
    print("Average spam confidence:", average_spam_confidence)
else:
    print("No lines with spam confidence found.")
