# Title: 숫자 만들기
# Link: https://www.acmicpc.net/problem/1511

import sys


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(cards: list):
    ans = [10]
    total_count = sum(cards)
    cards = list(map(list, zip(range(10), cards)))

    while total_count:
        for i in range(9, -1, -1):
            select_number, select_count = cards[i]
            if select_count <= 0 or select_number == ans[-1]:
                if select_number == 0:
                    total_count -= 1
                continue
            ans.append(select_number)
            cards[i][1] -= 1
            max_card, max_count = max(cards, key=lambda x: [x[1], x[0]])
            total_count -= 1

            if len(ans) > 2 and max_card == ans[-2]:
                break

            # check if the over half of same card in the rest cars
            if max_count*2 > total_count+1:
                ans.pop()
                cards[i][1] += 1
                ans.append(max_card)
                cards[max_card][1] -= 1
            break

    ans = ans[1:]
    while ans and ans[0] == 0:
        ans = ans[1:]
    if not ans:
        return '0'
    return ''.join(map(str, ans))


def main():
    cards = read_list_int()
    print(solution(cards))


if __name__ == '__main__':
    main()