import unittest
from day15 import calc


class Test(unittest.TestCase):
    def test_day15(self):
        self.assertEqual(calc(), 1320, "1320 is the sum of results")


if __name__ == '__main__':
    unittest.main()
