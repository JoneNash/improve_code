#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/1/10 10:50
"""

def binary_search1(nums,item):
    """二分查找 非递归方式"""
    n=len(nums)
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if item<nums[mid]:
            end=mid-1
        elif item>nums[mid]:
            start=mid+1
        else:
            return True

def binary_search2(nums,item):
    n = len(nums)
    if 0 == n:
        return False
    mid=n//2

    if item<nums[mid]:
        return binary_search2(nums[:mid],item)
    elif item>nums[mid]:
        return binary_search2(nums[mid+1:],item)
    else:
        return True

print binary_search1([1,4,8,3,5,6,2,9],5)
print binary_search2([1,4,8,3,5,6,2,9],5)