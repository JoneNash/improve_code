#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/11/27 8:14 PM
"""

def lengthOfLongestSubstring(s):
    dct = {}
    max_so_far = curr_max = start =0
    for index, i in enumerate(s):

        #dct[i]>=start解决"abcba"这种中间有元素重复的情况
        if i in dct and dct[i]>=start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dct[i]
            #如果元素有重复，则从重复元素下一个位置开始
            start=dct[i]+1

        else:
            curr_max += 1
        dct[i] = index
    return max(max_so_far, curr_max)

if __name__ == '__main__':
    s='abcba'
    print "result: ",lengthOfLongestSubstring(s)