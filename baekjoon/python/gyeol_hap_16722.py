# Title: 결! 합!
# Link: https://www.acmicpc.net/problem/16722

import sys
import enum
import itertools

sys.setrecursionlimit(10 ** 6)


read_list_words = lambda: sys.stdin.readline().strip().split(' ')
read_single_int = lambda: int(sys.stdin.readline().strip())


class Shape(enum.Enum):
    CIRCLE = 0
    SQUARE = 1
    TRIANGLE =2


class Color(enum.Enum):
    YELLOW = 0
    RED = 1
    BLUE = 2
    GRAY = 3
    WHITE = 4
    BLACK = 5


class Card:
    def __init__(self, num: int, shape: Shape, shape_color: Color, bg_color: Color):
        if shape == 'CIRCLE':
            self.shape = Shape.CIRCLE
        elif shape == 'TRIANGLE':
            self.shape = Shape.TRIANGLE
        elif shape == 'SQUARE':
            self.shape = Shape.SQUARE

        if shape_color == 'YELLOW':
            self.sh_color = Color.YELLOW
        elif shape_color == 'RED':
            self.sh_color = Color.RED
        elif shape_color == 'BLUE':
            self.sh_color = Color.BLUE

        if bg_color == 'GRAY':
            self.bg_color = Color.GRAY
        elif bg_color == 'WHITE':
            self.bg_color = Color.WHITE
        elif bg_color == 'BLACK':
            self.bg_color = Color.BLACK
        self.number = num


def make_hap_list(deck: list):
    ans = []
    for a, b, c in itertools.combinations(deck, 3):
        is_shape, is_sh_color, is_bg_color = False, False, False
        if a.shape == b.shape == c.shape or len(set([a.shape, b.shape, c.shape])) == 3:
            is_shape = True
        if a.sh_color == b.sh_color == c.sh_color or len(set([a.sh_color, b.sh_color, c.sh_color])) == 3:
            is_sh_color = True
        if a.bg_color == b.bg_color == c.bg_color or len(set([a.bg_color, b.bg_color, c.bg_color])) == 3:
            is_bg_color = True
        if is_bg_color and is_sh_color and is_shape:
            ans.append((a.number, b.number, c.number))
    return ans


def solution(deck: list, plays: list):
    score = 0
    haps = make_hap_list(deck)
    called_haps = []
    called_gyeol = False
    for play in plays:
        if play[0] == 'H':
            nums = tuple(map(int, sorted([play[1], play[2], play[3]])))
            if nums not in called_haps and nums in haps:
                score += 1
                called_haps.append(nums)
            else:
                score -= 1
        else:
            if len(called_haps) == len(haps) and not called_gyeol:
                score += 3
                called_gyeol = True
            else:
                score -= 1
    return score


def main():
    deck = []
    for i in range(1, 10):
        shape, sh_color, bg_color = read_list_words()
        deck.append(Card(i, shape, sh_color, bg_color))
    plays = []
    n = read_single_int()
    for _ in range(n):
        plays.append(read_list_words())

    print(solution(deck, plays))


if __name__ == '__main__':
    main()