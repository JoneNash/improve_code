#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/11/28 7:07 PM
@info: 最长公共子序列问题
"""

#DP方法
def findLength( A, B):
    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

    print dp
    return max(max(row) for row in dp)


if __name__ == '__main__':

    A=[1,2,3,4,5,7,8,10,11]
    B=[1,2,3,4,7,9,10,11]

    print findLength(A,B)