import random

def main():
    n = random.randint(1, 10)
    print(n)
    for _ in range(n):
        s = [random.randint(0, 1) for _ in range(random.randint(1, 10))]
        print(''.join(map(str, s)))


if __name__ == "__main__":
    main()