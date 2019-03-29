#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/5 10:14
"""

class Solution:
    def jumpFloor(self, number):
        arrs=[0]*(number+1)
        print 'arrs : ',arrs

        for i in range(1,number+1):
            if i ==1:
                arrs[i]=1
            elif i==2:
                arrs[i]=2
            else:
                arrs[i]=arrs[i-1]+arrs[i-2]

        print 'arrs : ', arrs
        return arrs[-1]




if __name__ == '__main__':
    s=Solution()
    print s.jumpFloor(10)