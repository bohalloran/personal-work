'''
Created on 30 Nov 2015

@author: bohalloran
'''

import unittest
from encode_string import EncodeString

class TestEncodeString(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def testDefault(self):
        es = EncodeString()
        esString = es.encode()
        self.assertEqual(esString, 'a4b5c3a4')

    def testEmpty(self):
        es = EncodeString('')
        esString = es.encode()
        self.assertEqual(esString, '')

    def testSingle(self):
        es = EncodeString('a')
        esString = es.encode()
        self.assertEqual(esString, 'a1')

    def testSpecialChars(self):
        es = EncodeString('$!^&^%!$!*!^')
        esString = es.encode()
        self.assertEqual(esString,'$1!1^1&1^1%1!1$1!1*1!1^1')

    def testCommonName(self):
        es = EncodeString('Massachusetts')
        esString = es.encode()
        self.assertEqual(esString,'M1a1s2a1c1h1u1s1e1t2s1')
        es = EncodeString('James')
        esString = es.encode()
        self.assertEqual(esString,'J1a1m1e1s1')

    def testUsefulNumbers(self):
        es = EncodeString('123-45-678')
        esString = es.encode()
        self.assertEqual(esString,'112131-14151-1617181')
        es = EncodeString('(617)-555-1212')
        esString = es.encode()
        self.assertEqual(esString,'(1611171)1-153-111211121')
        es = EncodeString('ee27c959-98f0-11e5-b22a-3c15c2c956be')
        esString = es.encode()
        self.assertEqual(esString,
        'e22171c1915191-19181f101-112e151-1b122a1-131c11151c121c1915161b1e1')

if __name__ == "__main__":
    unittest.main()
