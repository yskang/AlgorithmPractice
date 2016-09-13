# Grade
# https://www.acmicpc.net/problem/9498

score = int(input())

result = ''
if score < 60:
    result = 'F'
elif score >= 60 and score < 70:
    result = 'D'
elif score >= 70 and score < 80:
    result = 'C'
elif score >= 80 and score < 90:
    result = 'B'
else:
    result = 'A'

print(result)
