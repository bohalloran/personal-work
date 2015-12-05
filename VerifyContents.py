"""
Created on 5 Dec 2015

@author: bohalloran
"""

import random
import csv

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
        self.randomResultList = []
        # TODO: Dicsuss with John.  Appears to be ambiguity in spec.
        # For now assume data set includes integers outside of upper
        # and lower limit bounds so we can get some error injection
        # TODO: Implement some kind of file cleanup from previous test run
        # Let's generate some test data with each test pass
        # TODO: In general need to put some exception handling around file I/O
        f = open(self.testFileName, 'w')
        for line in xrange(self.numLines):
            # Use random library as convenience mechanism
            randNum = random.randint((self.lowerLimit-10),(self.upperLimit+10))
            f.write(str(line+1) + '\t' + str(randNum) + '\n')
        f.close()

    def parseData(self):
        # Read data into list
        with open(self.testFileName, 'r') as f:
            # Use csv library as convenience mechanism
            reader=csv.reader(f,delimiter='\t')
            for lineNum, value in reader:
                self.randomResultList.append([lineNum,value.rstrip('\n')])

    def verifyData(self):
        # Let's now verify the data with range 100 <= n <= 500
        # TODO: Add writing results to pass.txt and fail.txt
        for i in self.randomResultList:
            if 100 <= int(i[1]) <= 500:
                # Decided to use the line number as part of descriptive name
                # makes it easier to locate
                print 'ValidateLine' + i[0] + ': Pass'
            else:
                print 'ValidateLine' + i[0] + ': Fail'
                print '\tLine' + i[0] + ' : Value ' + i[1]

    def generateDifferences(self):
        return

v = VerifyContents()
v.parseData()
v.verifyData()
v.generateDifferences()
