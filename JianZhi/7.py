#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/5 10:03
"""


class Solution:
    def Fibonacci(self, n):
        if(n==0):
            return 0
        if(n==1):
            return 1


        arr=[0,1]

        for i in range(2,n+1):
            arr.append(arr[i-1]+arr[i-2])

        return arr[n]

if __name__ == '__main__':
    print Solution().Fibonacci(30)