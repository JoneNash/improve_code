#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/10 21:47
"""


class Solution:
    def ReverseSentence(self, s):
        return " ".join(s.split(" ")[::-1])

if __name__ == '__main__':
    s=Solution()
    print s.ReverseSentence("student a am I")