#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/11/28 5:42 PM
"""

#Dynamic Programming

def longestPalindrome( s):
    """
    :type s: str
    :rtype: str
    """
    if not s: return s
    res = ''
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    max = 0
    for j in range(n):
        for i in range(0, j + 1):
            dp[i][j] = ((s[i] == s[j]) and ((j - i <= 2) or dp[i + 1][j - 1]))
            if dp[i][j]:
                if (j - i + 1) > max:
                    max = j - i + 1
                    res = s[i:j + 1]
    return res


def longestPalindromicSubString2(s):

    if not s:return s

    res = ''

    dp=[[False for _ in range(len(s))] for _ in range(len(s))]

    max=0


    for j in range(len(s)):
        for i in range(0,j+1):
            dp[i][j]=( (s[j]==s[i]) and ((j-1<=i+1) or dp[i+1][j-1])  )

            if dp[i][j]:
                if j-i+1>max:
                    max=j-i+1
                    res=s[i:j+1]

    return res
















if __name__ == '__main__':
    s='abcbadesesa'
    print longestPalindrome(s)
    print longestPalindromicSubString2(s)