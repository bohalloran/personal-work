'''
Created on 29 Nov 2015

@author: bohalloran
'''

import unittest
from matrix_cross_product import MatrixCrossProduct

class TestMatrixCrossProduct(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def testDefaultCorners(self):
        matrix = MatrixCrossProduct()
        testMatrix = matrix.loadMatrix()
        self.assertEqual(testMatrix[0][0], 1)
        self.assertEqual(testMatrix[2][0], 3)
        self.assertEqual(testMatrix[0][2], 3)
        self.assertEqual(testMatrix[2][2], 9)

if __name__ == "__main__":
    unittest.main()
