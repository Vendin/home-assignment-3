# -*- coding: utf-8 -*-

import unittest
from tests.calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

    def testAddition(self):
        cal = Calculator()
        result = cal.addition(0.001, 0.003)
        self.assertEqual(0.004, result)

    def testSubtraction(self):
        cal = Calculator()
        result = cal.subtraction(0.1, 0.001)
        self.assertEqual(0.099, result)

    def testMultiply(self):
        cal = Calculator()
        result = cal.multiply(0.001, 10)
        self.assertEquals(0.01, result)

    def testDivide(self):
        cal = Calculator()
        result = cal.divide(5, 1000)
        self.assertEquals(0.005, result)

    def testDivideError(self):
        cal = Calculator()
        self.assertRaises(ValueError, cal.divide, 10, 0)

    def testLogMyMore(self):
        cal = Calculator()
        result = cal.logMy(25, 5)
        self.assertEquals(2, result)

    def testLogMyLess(self):
        cal = Calculator()
        result = cal.logMy(0.125, 2)
        self.assertEquals(-3, result)

    def testLog(self):
        cal = Calculator()
        log1 = cal.logMath(12223, 2)
        log2 = cal.logMy(12223, 2)
        self.assertEquals(round(log1, 5), log2)

    def testLogMyErrorOne(self):
        cal = Calculator()
        self.assertRaises(ValueError, cal.logMy, 100, 0)

    def testLogMyErrorTwo(self):
        cal = Calculator()
        self.assertRaises(ZeroDivisionError, cal.logMy, 100, 1)

    def testLogMathMore(self):
        cal = Calculator()
        result = cal.logMath(25, 5)
        self.assertEquals(2, result)

    def testLogMathLess(self):
        cal = Calculator()
        result = cal.logMath(0.125, 2)
        self.assertEquals(-3, result)

    def testLogMathErrorOne(self):
        cal = Calculator()
        self.assertRaises(ValueError, cal.logMath, 100, 0)

    def testLogMathErrorTwo(self):
        cal = Calculator()
        self.assertRaises(ZeroDivisionError, cal.logMath, 100, 1)
