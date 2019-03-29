#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/6 15:27
"""

class Solution:
    def rectCover(self, number):
        # write code here
        res = [0, 1, 2]
        while len(res)<=number:
            res.append(res[-1]+res[-2])
        return res[number]


if __name__ == '__main__':
    print Solution().rectCover(10)