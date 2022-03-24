# Year 2007
# https://www.acmicpc.net/problem/1924

line = input()
month = int(line.split(' ')[0])
day = int(line.split(' ')[1])

dayOfWeek = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}
dayOfMonth = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

#1/1:Mon

days = 0
for m in range(1, month):
    days = days + dayOfMonth[m]
 
print(dayOfWeek[(day + days)%7])    
