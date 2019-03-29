#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/11/28 8:31 PM
"""

def lengthOfLIS( nums):
    if not nums: return 0
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            # print i,j
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == '__main__':
    A = [3, -1, 4, -6, 5]
    print lengthOfLIS(A)