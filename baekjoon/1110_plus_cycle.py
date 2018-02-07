# https://www.acmicpc.net/problem/1110

def get_new_number(num):
    sum_of_each = int(num[0]) + int(num[1])
    return str(num[1]) + str(sum_of_each%10)

def get_cycle(n):
    n = '{:02d}'.format(int(n))
    target = n
    count = 1
    new_number = get_new_number(n)
    while new_number != target:
        n = new_number
        new_number = get_new_number(n)
        count+=1
    return count

print(get_cycle(input()))
