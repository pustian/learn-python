#!/usr/bin/env python

def is_prime(x):
    ''' 对正整数作是否是质数的判断 '''
    if x == 2 or x == 3:
        return True
    else:
        if x % 2 == 0:
            return False
        else:
            for i in range(3, int((x+1)/2), 2 ) :
                print("x=%d i=%d" %(x, i))
                if( x % i == 0) :
                    return False
    return True

x = int(input("输入一个正整数"))
if(is_prime(x) ):
    print("%d 是质数" % x)
else:
    print("%d 是合数" % x)

