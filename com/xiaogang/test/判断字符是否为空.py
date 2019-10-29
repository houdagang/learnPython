import datetime
a = '9:00'
b = '11:30'

time_a = datetime.datetime.strptime(a,'%H:%M')
time_b = datetime.datetime.strptime(b,'%H:%M')

print(time_a)
print(time_b)
if time_a > time_b:
    print(1)
else:
    print(2)

time = b.split(':')
day1.extend(time)



time1 = datetime.datetime(int(day1[0]),int(day1[1]),int(day1[2]),int(day1[3]),int(day1[4]))
time2 = datetime.datetime(int(day2[0]),int(day2[1]),int(day2[2]),int(day2[3]),int(day2[4]))
print(time1)
print(time2)

print(time1.__ge__(time2))