#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/1/10 10:27
冒泡排序
"""


def bubble_sort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num

print bubble_sort([5,4,6,3,1,2])