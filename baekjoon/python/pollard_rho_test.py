import random, math, timeit


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def f1(x, n):
    return (x * x - 1) % n


def f2(x, n):
    return (x * x + 1) % n


def f3(x, n):
    return (x * x * x - 1) % n


def f4(x, n):
    return random.randint(0, n)


# http://en.wikipedia.org/wiki/Ulam_spiral#Hardy_and_Littlewood.27s_Conjecture_F
def f5(x, n):
    return (4 * x * x - 2 * x + 41) % n


def f6(x, n): return (x + 1) % n


def f7(x, n): return (x + 2) % n


def f8(x, n): return (x + int(math.sqrt(n))) % n


def f9(x, n): return (2 ** x) % n


def f10(x, n): return (2 ** x + 1) % n


def f11(x, n): return (x * 2) % n


def f12(x, n): return (x * 3) % n


def f13(x, n): return (x + 3) % n


def f14(x, n): return (x * 4) % n


def f15(x, n): return (x ** 2 + 3) % n


def f16(x, n): return (x + int(math.sqrt(x)) + 1) % n


def rho(n, f=f1):
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = gcd(abs(x - y), n)
    if d == n:
        return False
    return d


def prime_factors(n):
    factors = set()
    i = 2
    while i * i <= n:
        while (n % i) == 0:
            factors.add(i)
            n = n / i
        i += 1
    if n > 1:
        factors.add(n)
    return factors


# returns how many times (in percentual), a function f fails when used by
# pollars rho method for numbers up to n
def test_correct(f, n=100):
    fail_count = 0
    for i in range(2, n):
        rho_i = rho(i, f)
        if not rho_i:
            factors = prime_factors(i)
            if len(factors) != 1:
                # print('return False but {} is not prime number'.format(i))
                fail_count += 1
        else:
            if i % rho_i != 0:
                # print('return wrong answer {} for number {}'.format(rho_i, i))
                fail_count += 1
    return 100 * fail_count / float(n)


# function to be used by benchmark. runs rho using f from 2 to n.
def benchmark(f, n):
    for i in range(2, n):
        rho_i = rho(i, f)


if __name__ == '__main__':
    n = 10000
    for f in f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16:
        function_name = f.__name__
        fails = str(test_correct(f, n)) + "%"
        # performance = timeit.timeit("benchmark({}, {})".format(function_name, n),
        #                             setup="from __main__ import rho, {}, benchmark".format(function_name))
        start_time = timeit.default_timer()
        benchmark(f, n)
        end_time = timeit.default_timer()

        print("Function: {}, Fails: {}, Performance: {}, n={}".format(function_name, fails, end_time - start_time, n))
