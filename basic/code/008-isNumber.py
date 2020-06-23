#!/usr/bin/env python
# -*- coding:utf-8 -*-

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(x)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试字符串和数字
print("foo %s" % is_number('foo'))   # False
print("1   %s" % is_number('1'  ))     # True
print("1.3 %s" % is_number('1.3'))   # True
print("1e3 %s" % is_number('1e3'))   # True
print("j   %s" % is_number('j'  ))   # True
print("1+j %s" % is_number('1+j'))   # True
print("-1.2 %s" % is_number('-1.2')) # True

print("以下unicode测试 python2 python3 返回不一致")
# 测试 Unicode
# 阿拉伯语 5
print("0 %s" % is_number('٥'))  # True
# 泰语 2
print("๒ %s" % is_number('๒'))  # True
# 中文数字
print("四 %s" % is_number('四')) # True
# 版权号
print("© %s" % is_number('©'))  # False
