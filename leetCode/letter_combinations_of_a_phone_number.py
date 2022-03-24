# Title: Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Problem:
    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_dict = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = ['']
        new_ans = []
        for digit in digits:
            for letter in digit_dict[int(digit)]:
                for e in ans:
                    new_ans.append(e+letter)
            ans, new_ans = new_ans, []
        return ans


def solution():
    digits = '234'
    problem = Problem()
    return problem.letter_combinations(digits)


def main():
    print(solution())


if __name__ == '__main__':
    main()
