
"""
Created on 30 Nov 2015

@author: bohalloran
"""

"""
The Fibonacci sequence of numbers is the following: 1, 1, 2, 3, 5, 8, 13,
21, 34, 55, ...

The first Fibonacci number, F_1, is 1.
The second Fibonacci number, F_2, is also 1.
For all other positive integers n, F_n is defined to be:
    F_n = F_(n-1) + F_(n-2)

That is, each Fibonacci number is the sum of the numbers preceding it in
the series.  Write a Python function fib(n) that returns the nth Fibonacci
number.
"""

class Fibonacci(object):

    def __init__(self, num=3):
        self.num = num

    def fibonacci(self):
        a, b = 0, 1
        for i in range(0, self.num):
            temp = a
            a = b
            b = temp + b
        return a
