# -*- coding: utf-8 -*-

import unittest

from src.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator()

    def testAddition(self):
        result = self.cal.addition(0.001, 0.003)
        self.assertEqual(0.004, result)

    def testSubtraction(self):
        result = self.cal.subtraction(0.1, 0.001)
        self.assertEqual(0.099, result)

    def testMultiply(self):
        result = self.cal.multiply(0.001, 10)
        self.assertEquals(0.01, result)

    def testDivide(self):
        result = self.cal.divide(5, 1000)
        self.assertEquals(0.005, result)

    def testDivideError(self):
        self.assertRaises(ValueError, self.cal.divide, 10, 0)

    def testLogMyMore(self):
        result = self.cal.logMy(25, 5)
        self.assertEquals(2, result)

    def testLogMyLess(self):
        result = self.cal.logMy(0.125, 2)
        self.assertEquals(-3, result)

    def testLog(self):
        log1 = self.cal.logMath(0.221, 2.5)
        log2 = self.cal.logMy(0.221, 2.5)
        self.assertEquals(round(log1, 5), log2)

    def testLogMyErrorOne(self):
        self.assertRaises(ValueError, self.cal.logMy, 100, 0)

    def testLogMyErrorTwo(self):
        self.assertRaises(ZeroDivisionError, self.cal.logMy, 100, 1)

    def testLogMathMore(self):
        result = self.cal.logMath(25, 5)
        self.assertEquals(2, result)

    def testLogMathLess(self):
        result = self.cal.logMath(0.125, 2)
        self.assertEquals(-3, result)

    def testLogMathErrorOne(self):
        self.assertRaises(ValueError, self.cal.logMath, 100, 0)

    def testLogMathErrorTwo(self):
        self.assertRaises(ZeroDivisionError, self.cal.logMath, 100, 1)
