import sys

if __name__ == '__main__':
    x = int(sys.stdin.readline().strip())
    if x == 1:
        print(0)
    else:
        count = 0
        pool = [False for _ in range(x+1)]
        ns = [x]
        temp = []
        found = False

        while not found:
            for n in ns:
                if not pool[n-1]:
                    if n-1 == 1:
                        found = True
                        break
                    pool[n-1] = True
                    temp.append(n-1)
                if n % 2 == 0 and not pool[n//2]:
                    if n // 2 == 1:
                        found = True
                        break
                    pool[n//2] = True
                    temp.append(n//2)
                if n % 3 == 0 and not pool[n//3]:
                    if n // 3 == 1:
                        found = True
                        break
                    pool[n//3] = True
                    temp.append(n//3)
            ns = temp
            temp = []
            count += 1
        print(count)