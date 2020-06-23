#!/usr/bin/env python
# -*- coding: utf-8 -*-

# n!= n*(n-1)*(n-2)*...*2*1
def factorial(n):
    res = 1;
    for x in range(1, n + 1):
        res = int(x) * res;
    return res;

x = int(input("输入正整数x=") );
print("x! = %d" % factorial(x) );
