#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/5 09:40
"""

class Solution:
    def minNumberInRotateArray1(self, rotateArray):
        if not rotateArray:
            return 0
        return min(rotateArray)

    def minNumberInRotateArray2(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        elif length == 1:
            return rotateArray[0]
        else:
            for i in range(length - 1):
                if rotateArray[i] > rotateArray[i + 1]:
                    return rotateArray[i + 1]
            return rotateArray[length - 1]



if __name__ == '__main__':
    s=Solution()
    print s.minNumberInRotateArray2([3,4,5,6,1,2])