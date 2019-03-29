#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/6 15:14
"""
class Solution:
    def jumpFloor(self, number):
        arrs=[0]*(number+1)

        if number==1:
            return 1
        elif number==2:
            return 2
        else:

            arrs[1]=1
            arrs[2] = 2

            for i in range(3,number+1):
                r=0
                for j in range(1,i):
                    r=r+arrs[j]
                arrs[i]=r+1

            return arrs[-1]






if __name__ == '__main__':
    s=Solution()
    print s.jumpFloor(10)

