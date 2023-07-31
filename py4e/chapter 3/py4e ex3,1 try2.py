hrs = input('number of hours worked: ')
rt= input('rate per hour: ')
hours = float (hrs)
rate = float (rt)
pay = hours * rate
if hours>40:
    over_time_pay= (hours - 40)* (rate*1.5)
    print (over_time_pay+400)
if hours<40:
    print('regular:', pay)