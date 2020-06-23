#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 以下实例为通过用户输入数字，并计算二次方程：
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

import math;
import cmath;

print("ax^2 + bx + c = 0 求跟")
a = input("输入整数a")
b = input("输入整数b")
c = input("输入整数c")
print("%dx^2 + %dx + %d = 0 " %(a, b, c) )

# a <> 0 
# delta = b*b - 4ac
# delta > 0  (-b + delat^1/2)/2a,  (-b -delat^1/2)/2a
# delta < 0  虚数
if( a == 0):
    if( b == 0):
        if( c == 0):
            print("任意解")
        else:
            print("无满足解")
    else:
        if( c == 0):
            print("x = 0")
        else:
            print("x = %f" %(-1.0*c/b) )
else:
    delta = b*b - 4.0*a*c
    if(abs(delta) < 1e-6):
        sqrt_delta = cmath.sqrt(delta)
        x1 = (-b+sqrt_delta)/(2*a)
        x2 = (-b-sqrt_delta)/(2*a)
        print("x1 = %f+%fi x2=%f+%fi" % (x1.real, x1.imag, x2.real, x2.imag) )
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b+sqrt_delta)/(2*a)
        x2 = (-b-sqrt_delta)/(2*a)
        print("x1 = %f x2=%f" % (x1, x2) )

