#%%
def sort_dots(dots: list, min_dot):

    if len(dots) <= 1:
        return dots
    else:
        h = len(dots) // 2
        a = sort_dots(list(dots)[:h], min_dot)
        b = sort_dots(list(dots)[h:], min_dot)
        temp = []
        ia, ib = 0, 0
        while ia < len(a) and ib < len(b):
            if ccw(min_dot, a[ia], b[ib]) > 0:
                temp.append(a[ia])
                ia += 1
            else:
                temp.append(b[ib])
                ib += 1
        if ia == len(a):
            temp += b[ib:]
        else:
            temp += a[ia:]
        return temp


def ccw(a, b, c):
    if b < c:
        return 1
    else:
        return -1


print(sort_dots([1,12,3,14,15,6,7], 0))

#%%
from dateutil import parser
import datetime
d = parser.parse('2019-04-16-14:01:45.2454')
# d = datetime.datetime(2018, 8, 30, 1, 26, 55, 731039)
print(d.strftime('%Y-%m-%d %H:%M:%S.%f'))


#%%
from dateutil import parser
import datetime
d1 = parser.parse('2019-04-16-14:01:45.2454')
d2 = parser.parse('2019-04-16-14:01:46.2455')

td =  d1 -d2

print(td.total_seconds())

#%%
import datetime
a = '2019-04-16-14-01-45-245433'.split('-')
d = datetime.datetime(*map(int, a))
print(d.strftime('%Y-%m-%d %H:%M:%S.%f'))

#%%
print('hello world')

#%%
