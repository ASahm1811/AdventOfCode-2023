import unittest
from day23 import calc


class Test(unittest.TestCase):
    def test_day23(self):
        self.assertEqual(calc(), 82)  # add assertion here


