#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_milti_table():
    for i in range(1, 10):
        for j in range(1, 10):
            print("{} x {} = {}\t".format(i, j, i*j), end="");
        print()

def print_milti_table_down_triangle():
    for i in range(1, 10):
        for j in range(1, 10):
            if(i >= j) :
                print("{} x {} = {}\t".format(i, j, i*j), end="");
        print()

print("全输出")
print_milti_table();
print("下三角输出")
print_milti_table_down_triangle();
