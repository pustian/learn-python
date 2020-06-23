#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math, cmath;

num = input("input a number:");
if(num > 0) :
    sqrt_num = math.sqrt(num);
    print("num=%f sqrt=%f" % (num, sqrt_num))
else:
    sqrt_num = cmath.sqrt(num);
    print("num=%f sqrt=%f + %fj" % (num, sqrt_num.real, sqrt_num.imag))

