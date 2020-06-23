#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 1, 1, 2, 3, 5
# f(n) = f(n-1) +f(n-2)
def fibonacci(n):
    if (1  == n or 2 == n):
        return 1;
    else:
        return fibonacci(n-1) + fibonacci(n-2);

def fibonacci2(n):
    if (1  == n or 2 == n):
        return 1;
    else:
        f_1 = 1;
        f_2 = 1;
        res = 0;
        count = 2;
        while count < n:
            res = f_1 + f_2;
            f_2 = f_1;
            f_1 = res;
            count += 1;
            # print("%d %d %d %d %d" %(count, n, res , f_1, f_2) )
        return res;
# x = int(input("输入一个正整数"))
# print("fibonacci({})={}".format( x, fibonacci(x) ) );

print("注意时间")
# items = int(input("输入输出项"))
for x in range(1, 40):
    print("{} fibonacci2 {} ".format( x, fibonacci2(x)) );
    
for x in range(1, 40):
    print("{} fibonacci {} ".format( x, fibonacci(x)) );
