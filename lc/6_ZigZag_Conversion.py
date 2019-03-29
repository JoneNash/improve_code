#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/12/9 3:55 PM
"""

def convert( s, numRows):

    if numRows==1: return s

    s_line_new=['']*numRows

    index,step =0,-1

    for c in s:
        s_line_new[index]=s_line_new[index]+c

        if index % (numRows-1)==0:
            step=-step

        index = index + step

    return ''.join(s_line_new)


if __name__ == '__main__':
    s='abcdefgh'
    s='a'
    print convert(s,1)