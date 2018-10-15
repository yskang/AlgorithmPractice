# Grade
# https://www.acmicpc.net/problem/9498

score = int(input())

result = ''
if score < 60:
    result = 'F'
elif 60 <= score < 70:
    result = 'D'
elif 70 <= score < 80:
    result = 'C'
elif 80 <= score < 90:
    result = 'B'
else:
    result = 'A'

print(result)
