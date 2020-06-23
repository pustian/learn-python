### Python 面向对象

- **类(Class):** 用来描述具有相同的属性和方法的对象的集合。

  > 它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。

- **类变量：**类变量在整个实例化的对象中是公用的。

  > 类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。

- **数据成员：**类变量或者实例变量, 用于处理类及其实例对象的相关的数据。

- **方法重写：**如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。

- **局部变量：**定义在方法中的变量。

- **实例变量：**在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。

- **继承：**即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。

- **实例化：**创建一个类的实例，类的具体对象。

- **方法：**类中定义的函数。

- **对象：**通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

### 创建类

```python
class ClassName:
   '类的帮助信息'   #类文档字符串
   class_suite  #类体 类成员，方法，数据属性组成。
```

类的帮助信息可以通过ClassName.__doc__查看

示例

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)
```

### 创建实例对象

### 访问属性

使用点号 **.** 来访问对象的属性。

你也可以使用以下函数的方式来访问属性：类似java中的反射

- getattr(obj, name[, default]) : 访问对象的属性。
- hasattr(obj,name) : 检查是否存在一个属性。
- setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
- delattr(obj, name) : 删除属性。

### Python内置类属性

- `__dict__` : 类的属性（包含一个字典，由类的数据属性组成）
- `__doc__` :类的文档字符串
- `__name__`: 类名
- `__module__`: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
- `__bases__` : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

### python对象销毁(垃圾回收)

使用了引用计数这一简单技术来跟踪和回收垃圾。

析构函数 `__del__` ，`__del__`在对象销毁的时候被调用，当对象不再被使用时，`__del__`方法运行：

https://www.jianshu.com/p/c608dee78ec8

https://zhuanlan.zhihu.com/p/83251959



### 通用的功能

| 序号 | 方法, |描述 | 简单的调用                                      |
| --- | ---|---|---|
| 1| `__init__ ( self [,args...] )` |构造函数|简单的调用方法: obj = className(args)|
| 2| `__del__( self )` |析构方法,删除一个对象|简单的调用方法 : `del obj`|
| 3| `__repr__( self )` |转化为供解释器读取的形式|简单的调用方法 : `repr(obj)`|
| 4| `__str__( self )` |用于将值转化为适于人阅读的形式 |简单的调用方法 : `str(obj)`|
| 5| `__cmp__ ( self, x )` |对象比较 |简单的调用方法 : `cmp(obj, x)`|

## 类的继承

继承创建的新类称为**子类**或**派生类**，被继承的类称为**基类**、**父类**或**超类**。

### 创建派生类

```python
class 派生类名(基类名)
    ...

class SubClassName (ParentClass1[, ParentClass2, ...]):
    ...
```

### 类属性与方法

##### 类的私有属性

`__private_attrs`：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 `self.__private_attrs`

##### 类的方法

在类的内部，使用 **def** 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数

##### 类的私有方法

`__private_method`：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 `self.__private_methods`

##### 访问私有数据

Python不允许实例化的类访问私有数据，但你可以使用 **object._className__attrName**（ **对象名._类名__私有属性名** ）访问属性，

##### 保护属性/方法

> 仅可以被类本身和继承字类使用

`_protected_attrs`

`_protected_method`