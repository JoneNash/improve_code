#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/1/12 09:39
绳子最多覆盖多少个点
https://www.cnblogs.com/mickole/articles/3579215.html

"""

def get_most_node(line,L):
    n=len(line)
    if(n==0):
        return 0
    start=0
    end=0
    max=0
    tmp_start=0
    tmp_end = 0
    while(start<=n-1 and end<=n-1):
        print start,'~~~',end
        if(line[end] - line[start]<=L):
            if(max < end - start+1):
                max = end - start+1
                tmp_start = start
                tmp_end = end
            end=end+1
        else:
            start=start+1
    if(end==n-1):
        print 'Line:',line[tmp_start:]
    else:
        print 'Line::',line[tmp_start:tmp_end+1]
    return max


line=[1,2,5,7,9,11,12,13,14,15,16,17,18,20,22,24]
L=6
print get_most_node(line,L)