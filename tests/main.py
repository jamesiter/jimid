#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tests
import unittest


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


if __name__ == '__main__':
    suite = tests.load_tests(unittest.TestLoader(), unittest.TestSuite())
    unittest.TextTestRunner(verbosity=2).run(suite)
