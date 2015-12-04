"""
Created on 30 Nov 2015

@author: bohalloran
"""

import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def testDefault(self):
        f = Fibonacci()
        res = f.fibonacci()
        self.assertEqual(res, 2)

    def testFifth(self):
        f = Fibonacci(5)
        res = f.fibonacci()
        self.assertEqual(res, 5)

    def testSeventh(self):
        f = Fibonacci(7)
        res = f.fibonacci()
        self.assertEqual(res, 13)

if __name__ == "__main__":
    unittest.main()
