#!/usr/bin/env python
# -*- coding:utf-8 -*-

print("输入三角形的三条边长");
a = input("输入边a=");
b = input("输入边b=");
c = input("输入边c=");

if ( (a+ b > c) and (a + c > b) and (b+c >a) ) :
    print("Triangle a=%f b=%f c=%f" % (a,b,c) ) ;
    # 计算半周长
    s = (a + b + c) / 2 ;
    # 计算面积
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 ;
    print("area=%f" % area);
else:
    print("不能组成三角形");

