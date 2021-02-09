# Title: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/

class Problem:
    def is_valid(self, s: str) -> bool:
        last_len = len(s)
        while s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if len(s) == last_len:
                break
            last_len = len(s)
        return not len(s)


def solution():
    s = "()[[]{}]{"
    problem = Problem()
    return problem.is_valid(s)


def main():
    print(solution())


if __name__ == '__main__':
    main()