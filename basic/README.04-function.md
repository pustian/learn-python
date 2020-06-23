内建函数

### 自定义函数语法

```python
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

> 默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。

### 函数调用

> 定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
>
> 这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。

### 参数传递

python 中一切都是对象

> 可变参数---python 传不可变对象实例
>
> 不可变参数---传可变对象实例

#### 参数

##### 必备参数

必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

##### 关键字参数

关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
 
#调用printinfo函数
printinfo( age=50, name="miki" )
```

##### 默认参数

> 调用函数时，默认参数的值如果没有传入，则被认为是默认值。



##### 不定长参数

需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数。

语法

```python 
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

示例

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
```

### 匿名函数

python 使用 lambda 来创建匿名函数。

语法

```python
lambda [arg1 [,arg2,.....argn]]:expression
```

示例

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
```

## return 语句

return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。

## 变量作用域

##### 全局变量

> 定义在函数内部的变量拥有一个局部作用域

##### 局部变量

> 定义在函数外的拥有全局作用域。