#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/11/28 8:35 PM

即：最长公共子序列问题
"""

def minDistance( w1, w2):
    common_string=[]
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if w1[i] == w2[j]:
                common_string.append(w1[i])
                dp[i + 1][j + 1]=dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    #输出公共子序列
    print common_string
    #公共子序列长度
    print 'size of longist common Subsequence:', dp[m][n]
    return m + n - 2 * dp[m][n]


if __name__ == '__main__':
    A = [3, -1, 4, -6, 5]
    B = [6, -1, 4, 7, 5]
    print minDistance(A,B)