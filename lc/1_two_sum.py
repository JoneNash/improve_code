#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/11/27 12:00 PM
"""


print"********\n"

def get_indexes_1(nums,target):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j

def get_indexes_2(nums,target):

    index_diff={}
    for i in range(len(nums)):
        if nums[i] in index_diff.keys():
            return index_diff.get(nums[i]),i
        else:
            index_diff[target-nums[i]]=i


if __name__ == '__main__':
    nums=(11,1,2,17,5,7,9)
    target=28
    print get_indexes_1(nums,target)
    print get_indexes_2(nums, target)
