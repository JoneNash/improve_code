#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/1/28 20:16

https://leetcode.com/problems/string-without-aaa-or-bbb/

"""

def strWithout3a3b( A, B):
    """
    :type A: int
    :type B: int
    :rtype: str
    """
    if A >= 2*B:
        return 'aab'* B + 'a'* (A-2*B)
    elif A >= B:
        return 'aab' * (A-B) + 'ab' * (2*B - A)
    elif B >= 2*A:
        return 'bba' * A + 'b' *(B-2*A)
    else:
        return 'bba' * (B-A) + 'ab' * (2*A - B)

print strWithout3a3b(2,10)