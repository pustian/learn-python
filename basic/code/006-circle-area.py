#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math;

print("输入圆的半径, 计算周长面积");
radius = input("圆半径")
circumference = math.pi * radius *2;
area = math.pi * radius * radius;

print("圆半径 %f 面积是 %f 周长 %f"  % (radius, area, circumference) );
