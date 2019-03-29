#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/8 22:28
"""

class Solution:

    def printMatrix(self, matrix):
        res=[]

        while matrix:
            #第一行
            res=res+matrix.pop(0)

            #最右边的列
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            #最后一行
            if matrix  and matrix[0]:
                res=res+matrix.pop()[::-1]

            #最左边的列
            if  matrix  and matrix[0]:
                for row in matrix[::-1]:
                    print row[0]
                    res.append(row.pop(0))
        return  res




if __name__ == '__main__':
    # matrix=[[1,2,3], [4,5,6], [7,8,9]]
    matrix = [[1,2],[3,4]]
    print Solution().printMatrix(matrix)