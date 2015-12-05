"""
Created on 5 Dec 2015

@author: bohalloran
"""

import random

"""
Class that examines the contents of a given file line by line to determine
if the range of randomly supplied values falls within acceptable limits.
"""

class VerifyContents(object):

    def __init__(self, testFileName = 'random_numbers.txt'):
        # TODO: Pass in file name from command line
        self.testFileName = testFileName
        self.differenceFilename = 'difference.txt'
        self.numLines = 1000
        self.lowerLimit = 100
        self.upperLimit = 500
        # TODO: Dicsuss with John.  Appears to be ambiguity in spec.
        # For now assume data set includes integers outside of upper
        # and lower limit bounds so we can get some error injection
        # TODO: Implement file cleanup from previous test run
        # Let's generate some test data with each test pass
        # TODO: In general need to put some exception handling around file I/O
        file = open(self.testFileName, 'w')
        for line in xrange(self.numLines):
            randNum = random.randint((self.lowerLimit-10),(self.upperLimit+10))
            file.write(str(line+1) + '\t' + str(randNum) + '\n')
        file.close()

    def parseVerifiyData(self):
        return

    def generateDifferences(self):
        return

v = VerifyContents()
v.parseVerifiyData()
v.generateDifferences()
