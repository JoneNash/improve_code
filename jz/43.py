#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/10 21:45
"""

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:]+s[:n]

if __name__ == '__main__':
    s=Solution()
    print s.LeftRotateString("AZDabce",3)