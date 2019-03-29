#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/1 14:45

https://blog.csdn.net/fuxuemingzhu/article/details/86667263

"""

def test_even_number(i):
    if(i & 1):
        return 'odd'
    else:
        return 'even'

if __name__ == '__main__':
    print test_even_number(11,)