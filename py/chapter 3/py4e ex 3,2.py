hrs = input('number of hours worked: ')
try:
    hours = float (hrs)
    rt= input('rate per hour: ')
    try:
        rate = float (rt)
        pay = hours * rate
        if hours>40:
            over_time_pay= (hours - 40)* (rate*1.5)
            print ('over time pay:', over_time_pay+400)
        if hours<40:
            print('regular pay:', pay)
    except :
        print ('please use figures')
except:
    print ('please use figures')