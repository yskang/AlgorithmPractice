# https://www.acmicpc.net/problem/2775


def number_of_people(k, n):
    belows = [0]*(n+1)
    currents = [0]*(n+1)
    for level in range(1, k+1):
        for i in range(1, n+1):
            if level == 1:
                currents[i] = i * (1+i)/2
            else:
                if i == 1:
                    currents[i] = belows[i]
                else:
                    currents[i] = currents[i-1] + belows[i]
        belows = currents
    return int(currents[n])


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        k = int(input())
        n = int(input())
        print(number_of_people(k, n))
