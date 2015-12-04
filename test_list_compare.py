"""
Created on 30 Nov 2015

@author: bohalloran
"""

import unittest
from list_compare import ListCompare

class TestListCompare(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def testDefault(self):
        comp = ListCompare()
        res = comp.comp()
        self.assertEqual(res, True)

    def testDifferentList(self):
        comp = ListCompare(list2=[3, 2, 5, 4])
        res = comp.comp()
        self.assertEqual(res, False)

    def testAssymetricList(self):
        comp = ListCompare(list1=[1, 2, 3, 4],list2=[1, 2, 3])
        res = comp.comp()
        self.assertEqual(res, False)

if __name__ == "__main__":
    unittest.main()
