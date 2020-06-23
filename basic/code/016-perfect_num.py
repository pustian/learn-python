#!/usr/bin/env python
# -*- coding:utf-8 -*-

# n位正整数等于其各位数字的n次方之和, 例如1^3 + 5^3 + 3^3 = 153。
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

def perfect_num(x):
    n = len(x);
    count = 0;
    res = 0;
    int_x  = int(x);
    while n > count:
        count += 1;
        remainer = int_x %10
        int_x = int_x /10
        res += remainer ** n;
    return res == int(x);

# print(perfect_num("1")  )
# print(perfect_num("9")  )
# print(perfect_num("153"))
# print(perfect_num("370"))
# print(perfect_num("10") )
for x in range(1, 1000000):
    if( perfect_num(str(x) ) ):
        print("%d" % x)
