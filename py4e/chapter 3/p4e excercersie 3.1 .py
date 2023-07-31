imp1 = input('number of hours worked: ')
imp2 = input('rate per hour: ')
hours= float(imp1)
rate= float(imp2)
regular_pay = hours*rate
if hours<=40:
    print('Pay:', regular_pay)
elif hours>40:
    new_rate = 10.0*1.5
    overtime = (hours-40)*new_rate
    new_pay = overtime + regular_pay
    print ('Pay:', '$',new_pay)