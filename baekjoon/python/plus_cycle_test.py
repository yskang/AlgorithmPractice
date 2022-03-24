import unittest
import baekjoon.plus_cycle_1110


class PlusCycleTestCase(unittest.TestCase):
    def test_get_new_number(self):
        ps = baekjoon.plus_cycle_1110.PlusCycle()
        self.assertEqual(ps.get_new_number("01"), "11")


if __name__ == '__main__':
    unittest.main()
