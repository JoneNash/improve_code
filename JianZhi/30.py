#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/14 14:54
"""

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if(len(array)==0):
            return None

        matrix=[]
        maxNum =max(array)
        for i in range(len(array)):
            matrix.append([0]*len(array))

        for i in range(len(array)):
            for j in range(i,len(array)):
                if(i==0):
                    matrix[i][j]=array[j]
                else:
                    matrix[i][j]=matrix[i-1][j-1]+array[j]

                if maxNum < matrix[i][j]:
                    maxNum = matrix[i][j]

        return maxNum



if __name__ == '__main__':
    arr=[6, -3, -2, 7, -15, 1, 2, 2]
    arr=[1,-2,3,10,-4,7,2,-5]
    print Solution().FindGreatestSumOfSubArray(arr)

