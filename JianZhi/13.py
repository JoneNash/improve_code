#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/6 16:24
"""

class Solution:
    def reOrderArray(self, array):
        even=[]
        odds=[]

        for i in array:
            if(i % 2==1):
                print i
                odds.append(i)
            else:
                print i
                even.append(i)

        return odds+even

if __name__ == '__main__':
    print Solution().reOrderArray([1,2,3,4,5])