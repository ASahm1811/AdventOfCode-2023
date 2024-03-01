import unittest
from day5 import calc


class Test(unittest.TestCase):

    def test_day5(self):
        self.assertEqual(calc(), 35, "35 is lowest location number")
