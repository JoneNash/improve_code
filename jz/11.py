#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/6 15:46
"""

class Solution:
    def NumberOf1(self, n):
        # write code here
        count=0

        flag=1

        while flag <= 0xffffffff:
            if(n & flag):
                print ":::",str(flag)
                count+=1
            flag=flag<<1
        return count


if __name__ == '__main__':
    print Solution().NumberOf1(-1)