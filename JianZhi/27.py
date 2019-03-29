#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/12 11:43
"""

class Solution:
    def Permutation(self, ss):
        # write code here
        res = []

        if(len(ss)<2):
            return ss

        for i in range(len(ss)):
            for n in map(lambda x: x+ss[i],self.Permutation(ss[:i]+ss[i+1:])):
                if n not in res:
                    res.append(n)

        return sorted(res)

if __name__ == '__main__':
    array='abcad'
    print Solution().Permutation(array)