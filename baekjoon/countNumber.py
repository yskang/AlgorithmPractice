a = int(input())
b = int(input())
c = int(input())
# a = 150
# b = 266
# c = 427

m = a * b * c
for i in range(10):
    print(str(str(m).count(str(i))))