#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 辗转相除法辗转相除法,又称欧几里德算法
# 先用较小的数对较大的数取余，再用余数对较小的数求余，直到余数为零
# 当余数为0的时候，最后的m即为最大公约数
def gcd(x, y):
    if(x < y):
        x,y = y,x

    while x % y != 0 and y != 0 :
        remainer = x % y              # 较小的数对较大的数取余
        x = y                         # 余数对较小的数求余
        y = remainer
        print("%d %d" %(x, y) )

    return y;

print(gcd(12, 18) )
print(gcd(2, 3) )
