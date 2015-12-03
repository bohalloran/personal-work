
'''
Created on 30 Nov 2015

@author: bohalloran
'''

class ListCompare(object):

    def __init__(self, list1=[1, 2, 3, 4], list2=[3, 2, 1, 4]):
        self.list1 = list1
        self.list2 = list2

    def comp(self):

        counter = 0
        res = True
        for i in self.list1:
            if i not in self.list2:
                counter += 1

        if counter > 0:
            res = False

        return res
