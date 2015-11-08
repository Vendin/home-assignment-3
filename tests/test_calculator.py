# -*- coding: utf-8 -*-

import unittest
from tests.calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

    def testAddition(self):
        cal = Calculator()
        result = cal.addition(5, 10)
        self.assertEqual(15, result)

    def testSubtraction(self):
        cal = Calculator()
        result = cal.subtraction(10, 5)
        self.assertEqual(5, result)

    def testMultiply(self):
        cal = Calculator()
        result = cal.multiply(10, 5)
        self.assertEquals(50, result)

    def testDivide(self):
        cal = Calculator()
        result = cal.divide(10, 5)
        self.assertEquals(2, result)

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
