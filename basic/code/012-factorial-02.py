#!/usr/bin/env python
# -*- coding: utf-8 -*-

# n!= n*(n-1)*(n-2)*...*2*1
def factorial(n):
    if n == 0 or n == 1:
        return 1;
    else:
        return factorial(n-1) * n;

x = int(input("输入正整数x=") );
print("x! = %d" % factorial(x) );
