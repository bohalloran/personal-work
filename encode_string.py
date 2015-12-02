'''
Created on 30 Nov 2015

@author: bohalloran
'''

# Class that encodes a string based on consecutive repetitions of a character.
# Eg: Input aaaabbbbbcccaaaa Gives an output a4b5c3a4

class EncodeString(object):

    def __init__(self, input='aaaabbbbbcccaaaa'):
        self.input = input
        self.results = []
        self.previous = ''
        self.encodedString = ''

    # if current character is same as previous character then increment counter
    # else if not equal then set counter to zero and assign a new charcter

    def encode(self):

        # parse string and count occurrences
        # stuff the results in an list of pairs
        for i in self.input:
            if i == self.previous:
                self.results[-1] = (i, self.results[-1][1] + 1)
            else:
                self.results.append((i, 1))
                self.previous = i

        # collect results into string
        for pair in self.results:
            self.encodedString += (pair[0] + str(pair[1])).rstrip('\n')

        return self.encodedString
