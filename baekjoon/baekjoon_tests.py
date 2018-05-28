import random
import unittest

import baekjoon.perfect_square_number_1977


class PerfectSquareNumber_1977(unittest.TestCase):
    def test_1(self):
        M = 60
        N = 100
        res = '245\n64'
        self.assertEqual(baekjoon.perfect_square_number_1977.perfect_square_number(M, N), res)

    def test_no_answer(self):
        M = 2
        N = 2
        res = '-1'
        self.assertEqual(baekjoon.perfect_square_number_1977.perfect_square_number(M, N), res)

    def test_min_max(self):
        M = 1
        N = 10000
        s = 0
        m = 9999999
        for i in range(1, 1000000):
            i_s = i * i
            if i_s > N:
                break
            s += i_s
            m = min(i_s, m)

        res = '{}\n{}'.format(s, m)
        self.assertEqual(baekjoon.perfect_square_number_1977.perfect_square_number(M, N), res)

    def test_1_diff_front(self):
        M = 1
        N = 2
        s = 1
        m = 1
        res = '{}\n{}'.format(s, m)
        self.assertEqual(baekjoon.perfect_square_number_1977.perfect_square_number(M, N), res)

    def test_1_diff_last(self):
        M = 9999
        N = 10000
        s = 10000
        m = 10000
        res = '{}\n{}'.format(s, m)
        self.assertEqual(baekjoon.perfect_square_number_1977.perfect_square_number(M, N), res)

    def test_0_diff(self):
        M = 1
        N = 1
        s = 1
        m = 1
        res = '{}\n{}'.format(s, m)
        self.assertEqual(baekjoon.perfect_square_number_1977.perfect_square_number(M, N), res)

    def test_random(self):
        count = 1000
        while count > 0:
            count -= 1
            M = random.randint(1, 10000)
            N = M + random.randint(0, 10000-M)
            s = 1
            m = 1
            res = '{}\n{}'.format(s, m)
            try:
                baekjoon.perfect_square_number_1977.perfect_square_number(M, N)
            except:
                print('fail on {}, {}'.format(M, N))


if __name__ == '__main__':
    unittest.main()
