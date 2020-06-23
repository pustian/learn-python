### 模块(Module)

Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

模块让你能够有逻辑地组织你的 Python 代码段。

把相关的代码分配到一个模块里能让你的代码更好用，更易懂。

模块能定义函数，类和变量，模块里也能包含可执行的代码。

### 模块的引入

模块定义好后，我们可以使用 import 语句来引入模块

```python
import module1[, module2[,... moduleN]]
```

 from 语句让你从模块中导入一个指定的部分到当前命名空间中

```python
from modname import name1[, name2[, ... nameN]]
```

把一个模块的所有内容全都导入到当前的命名空间

```
from modname import *
```

### 搜索路径

一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。



当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？

这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。

这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。

搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。



导入一个模块，Python 解析器对模块位置的搜索顺序是：

> - 1、当前目录
> - 2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
> - 3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
>
> 模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

```python
import sys
sys.path
```



### 调用模块中的函数

```python
模块名.函数名
```

### 命名空间和作用域

##### 命名空间

变量是拥有匹配对象的名字（标识符）。

命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。

一个 Python 表达式可以访问局部命名空间和全局命名空间里的变量。

如果一个局部变量和一个全局变量重名，则 `局部变量会覆盖全局变量`。

每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。

##### 作用域

Python 会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。

因此，如果要给函数内的全局变量赋值，必须使用 global 语句。



------

#### dir()函数

dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

返回的列表容纳了在一个模块里定义的所有模块，变量和函数。

```python
import math
content = dir(math)
print(content)
```

#### globals() 和 locals() 函数

根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。

如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

##### python2 --- reload() 函数

当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。

因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：

```python
reload(module_name)
```

###  `__name__`属性

一个模块被另一个程序第一次引入时，其主程序将运行。

```python
cat <<EOF >using_name.py
#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

def printMsg(msg)
    print(msg)
EOF
```

```python
import using_name
...
reload(using_name) 
```

```python
python using_name.py
```

### 标准模块

Python 本身带着一些标准的模块库

### Python中的包

包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。

比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。



包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 `__init__.py` 文件, 该文件的内容可以为空。`__init__.py`用于标识当前文件夹是一个包。

##### 包结构示例

```python
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

