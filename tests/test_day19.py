import unittest
from day19 import calc


class MyTestCase(unittest.TestCase):
    def test_day19(self):
        self.assertEqual(calc(), 19114, "19114 is the sum total")


if __name__ == '__main__':
    unittest.main()
