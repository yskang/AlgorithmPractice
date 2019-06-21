import random

def main():
    n = random.randint(1,10)
    print(n)
    for _ in range(n):
        print(random.randint(1, 10))

if __name__ == '__main__':
    main()