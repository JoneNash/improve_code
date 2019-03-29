#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/4 17:08

https://www.nowcoder.com/questionTerminal/54275ddae22f475981afa2244dd448c6
"""

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        self.stackA.append(node)


    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else :
            while(self.stackA):
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


if __name__ == '__main__':
    s=Solution()
    s.push(0)
    s.push(1)
    s.push(2)
    print s.pop()