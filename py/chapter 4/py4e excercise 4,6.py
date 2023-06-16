def computepay (hours,rate):
    if hours<=40:
        pay = hours*rate   
        return  pay
    if hours>40:
        reg_pay= hours*rate
        new_rate = 10.0*1.5
        overtime = (hours-40)*new_rate
        pay = overtime + reg_pay
        return pay
imp1 = input('number of hours worked: ')
imp2 = input('rate per hour: ')
try:
    hours= float(imp1)
    rate= float(imp2)
    pay = computepay(hours,rate)
    print ('Pay:', pay)
except:
    print ('input numbers')