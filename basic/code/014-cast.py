#!/usr/bin/env python
# -*-  coding:utf-8 -*-
x = input("输入一个十进制数")
dec_num = int(x)
bin_num = bin(dec_num)
oct_num = oct(dec_num)
hex_num = hex(dec_num)
print("string x={} \nint_num={} \nbin_num={} \noct_num={} \nhex_num={}".format(x, dec_num, bin_num, oct_num, hex_num))

x = input("请输入一个字符")
asc_ch = ord(x)

print("ord x={} asc_ch={}".format(x, asc_ch))
print("chr 97--asc_ch={}".format(chr(97)) )

