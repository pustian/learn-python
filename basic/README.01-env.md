## python3.6/7

https://docs.python.org/3/library/

### ipython3 安装
```bash
sudo apt install ipython3 ttf-bitstream-vera
sudo apt install python3-pip
```

### pip换源
#### 临时换源
```bash
# pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider
```
> 国内源
> + 清华：https://pypi.tuna.tsinghua.edu.cn/simple
> + 阿里云：http://mirrors.aliyun.com/pypi/simple/
> + 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
> + 华中理工大学：http://pypi.hustunique.com/
> + 山东理工大学：http://pypi.sdutlinux.org/ 
> + 豆瓣：http://pypi.douban.com/simple/

#### 永久修改
```bash
mkdir ~/.pip
cat <<EOF > ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
EOF
```
> windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini。内容同上。

### 安装库
```bash
pip3 install numpy
pip3 install pandas
pip3 install matplotlib
```
## python2.7

https://docs.python.org/2/library/

### ipython 安装
```bash
sudo apt install ipython
sudo apt install python-pip
```

### pip换源
#### 临时换源
```bash
# pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider
```
> 国内源
> + 清华：https://pypi.tuna.tsinghua.edu.cn/simple
> + 阿里云：http://mirrors.aliyun.com/pypi/simple/
> + 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
> + 华中理工大学：http://pypi.hustunique.com/
> + 山东理工大学：http://pypi.sdutlinux.org/ 
> + 豆瓣：http://pypi.douban.com/simple/

#### 永久修改
```bash
mkdir ~/.pip
cat <<EOF > ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
EOF
```
> windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini。内容同上。


pip install numpy
pip install pandas
pip install matplotlib
