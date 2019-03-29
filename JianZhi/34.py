#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/14 17:31
"""

class Solution:
    def FirstNotRepChar(self,s):

        if len(s)==0:
            return -1
        else:
            d={}

            for i in s:
                if d.has_key(i):
                    d[i]=d.get(i)+1
                else:
                    d[i] = 1

            for index,j in enumerate(s):
                if d[j]==1:
                    return index
            return -1



if __name__ == '__main__':
    s='abcdefgabcdef'
    s='aa'

    print Solution().FirstNotRepChar(s)