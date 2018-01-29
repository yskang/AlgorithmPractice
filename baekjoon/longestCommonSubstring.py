#
# https://www.acmicpc.net/problem/9249

str_a = input()
str_b = input()

if len(str_a) < len(str_b):
    str_a, str_b = str_b, str_a

dp = [0 for _ in range(len(str_a)+1)]
dp2 = [0 for _ in range(len(str_a)+1)]

max_len, max_end = 0, 0

for i in range(len(str_b)):
    for j in range(len(str_a)):
        if str_a[j] is str_b[i]:
            dp2[j+1] = dp[j] + 1
            if dp2[j+1] > max_len:
                max_end = j+1
                max_len = dp2[j+1]
        else:
            dp2[j+1] = 0
    print(dp2)
    dp, dp2 = dp2, dp

print(max_len)
print(str_a[max_end-max_len:max_end])