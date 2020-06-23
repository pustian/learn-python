#!/usr/bin/env python
# -*- coding:utf-8 -*-

def swap1(x, y):
    temp = x;
    x = y;
    y = temp;
    print("swap1 x=%f y=%f" %(x, y) )

def swap2(x, y):
    x, y = y, x
    print("swap2 x=%f y=%f" %(x, y) )

def swap3(x, y):
    x = x + y;
    y = x - y; # y = (x+ y) - y
    x = x - y; # x = (x+y) -[ (x+y) -y]
    print("swap3 x=%f y=%f" %(x, y) )

def swap4(x, y):
    if ( type(x) == int and type(y) == int):
        x = x ^ y;
        y = x ^ y; # y = x ^ y ^ y = x
        x = x ^ y; # x = x ^ y ^(x^ y ^ y) = y
        print("swap4 x=%f y=%f" %(x, y) )
    else:
        print("only suppert int")

x = input("输入数x=")
y = input("输入数y=")

swap1(x, y)
swap2(x, y)
swap3(x, y)
swap4(x, y)
print("x=%f y=%f" %(x, y) )

