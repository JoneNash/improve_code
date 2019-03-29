#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/11/28 8:08 PM
"""

def findMaxSubArray( A):
    for i in range(1,len(A)):
        if(A[i-1]>0):
            A[i]=A[i] +A[i-1]

    return max(A)


if __name__ == '__main__':

    A=[-2,1,-3,4,-1,2,1,-5,4]
    print findMaxSubArray(A)