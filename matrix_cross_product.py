'''
Created on 29 Nov 2015

@author: bohalloran
'''

# Class that calculates the cross product of an arbitrary matrix
# The first row increments each element in the row by one and
# likewise the first column increments by one.  The body of the
# matrix is the cross product of each element in the first row
# and first column.

class MatrixCrossProduct(object):

    # create matrix by default of three rows by three columns
    def __init__(self, numRows=3, numCols=3):
        self.numRows = numRows
        self.numCols = numCols
        self.matrix = []

    def loadMatrix(self):
        for i in xrange(self.numRows):
            self.matrix.append([])
            for j in xrange(self.numCols):
                self.matrix[i].append((i+1)*(j+1))
        return self.matrix
