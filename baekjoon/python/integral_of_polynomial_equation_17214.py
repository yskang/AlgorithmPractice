# Title: 다항 함수의 적분
# Link: https://www.acmicpc.net/problem/17214

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def get_coefficient_degree(term: str):
    degree = term.count('x')
    coefficient = term[0:len(term)-degree]
    if coefficient:
        coefficient = int(coefficient)
    else:
        coefficient = 1
    return coefficient, degree


def integral(term: str):
    coefficient, degree = get_coefficient_degree(term)
    if coefficient == 0:
        return ''
    coefficient = coefficient // (degree + 1)
    return ('' if coefficient == 1 else str(coefficient)) + 'x'*(degree+1)


def solution(equation: str):
    res = ''
    first_operator = ''
    if equation[0] == '-':
        first_operator = '-'
        equation = equation[1:]
    if equation.count('+') == 1:
        first_term, second_term = equation.split('+')
        res = first_operator + integral(first_term) + '+' + integral(second_term)
    elif equation.count('-') == 1:
        first_term, second_term = equation.split('-')
        res = first_operator + integral(first_term) + '-' + integral(second_term)
    else:
        res = first_operator + integral(equation)
    
    return res + ('+' if res != '' else '') + 'W'


def main():
    eq = read_single_str()
    print(solution(eq))


if __name__ == '__main__':
    main()