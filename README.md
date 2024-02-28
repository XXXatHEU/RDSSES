
# 可撤销的动态对称可搜索加密方案论文的实验项目
虚拟机：Ubuntu22.04LTS <br>
语言：Python3.7.9<br>
第三方库：Charm-Crypto+pypbc <br>
编程平台：Jupyter环境 <br>
其他依赖详情见文件 requirement.txt
## 环境搭建
### 1 前置工具

1. 为了方便本地操作，先安装openssh-server和net-tools

```shell
sudo apt install openssh-server net-tools -y
```

2. 连接到本地xshell以后，再进行如下安装

```shell
sudo apt install gcc g++ make vim vsftpd wget m4 flex bison python3-setuptools python3-dev python3-pip -y
```
安装python编译依赖
```shell
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev
```
3. 配置vsftpd

```shell
sudo vim /etc/vsftpd.conf
```

![image](https://github.com/XXXatHEU/RDSSES/assets/119908567/d62526a1-4577-41d7-acf4-b60f90d16f88)


4. 配置pip源

```shell
cd
sudo mkdir .pip
cd .pip
sudo touch pip.conf
sudo vim pip.conf
```

粘贴以下内容到pip.conf

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```

### 安装git

```shell
sudo apt install git
```

git配置

```shell
git config --global user.name 名字
git config --global user.email  邮箱
```

cd到家目录下的Downloads目录下，下载所有源码包

```shell
sudo wget https://gmplib.org/download/gmp/gmp-5.1.3.tar.bz2
sudo wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz
sudo wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz

# charm和pypbc获取
# 可以从github导入到gitee加快下载速度
git clone https://gitee.com/liihoo/charm.git
git clone https://gitee.com/liihoo/pypbc.git
```

### 安装GMP

```shell
sudo tar -jxvf gmp-5.1.3.tar.bz2
```

```shell
cd gmp-5.1.3/
```

```shell
sudo ./configure
```

```shell
sudo make
```

```shell
sudo make install
```

### 安装PBC

```shell
sudo tar -zxvf pbc-0.5.14.tar.gz
```

```shell
cd pbc-0.5.14/
```

```shell
sudo ./configure
```

```shell
sudo make
```

```shell
sudo make install
```


添加libpbc到系统链接库

```shell
sudo vim /etc/ld.so.conf
```
写入以下内容
```shell
/usr/local/lib
```

更新动态库

```shell
sudo ldconfig
```

### 安装Python3.7.9
新建一个文件用于安装目录，比如/opt/python3/python3.7.9
```shell
sudo tar -zxvf Python-3.7.9.tgz
```

```shell
sudo ./configure --prefix=/opt/python3/python3.7.9
```


```shell
sudo make
```

```shell
sudo make install
```

创建Python3.7.9的软连接。不要覆盖系统默认的版本

```shell
sudo ln -s /opt/python3/python3.7.9/bin/pip3 /usr/bin/pip3.7
```

```shell
sudo ln -s /opt/python3/python3.7.9/bin/python3.7 /usr/bin/python3.7
```

```shell
pip3.7 install pyparsing==2.2.1
```

### 安装Jupyter

```shell
pip3.7 install jupyter notebook
```

打开家目录下的.bashrc添加jupyter路径

```
vim .bashrc
```

![image](https://github.com/XXXatHEU/RDSSES/assets/119908567/42b13edf-073a-45c6-b4f9-d98e41718a19)


更新配置

```shell
source .bashrc
```

生成配置文件

```shell
jupyter notebook --generate-config
```

使用python中的`passwd()`创建密码，终端输入`ipython`打开ipython并输入，复制打印的密码

```python
In [1]: from notebook.auth import passwd
In [2]: passwd()
```

打开配置文件

```shell
vim ~/.jupyter/jupyter_notebook_config.py
```

在文件末尾添加：

```python
c.NotebookApp.allow_remote_access = True #允许远程连接
c.NotebookApp.ip='*' # 设置所有ip皆可访问
c.NotebookApp.open_browser = False # 禁止自动打开浏览器
c.NotebookApp.port =8888 #任意指定一个端口
c.NotebookApp.password = u'sha:..' #之前复制的密码
```

### 安装charm-crypto

打开charm-crypto的[GitHub](https://github.com/JHUISI/charm)地址，下载源码的压缩包

![image](https://github.com/XXXatHEU/RDSSES/assets/119908567/08423753-3d76-40a8-9105-ee7403654b8a)


网络原因，需要想办法，最后打开xftp上传到Ubuntu

```shell
sudo unzip charm-dev.zip
```

```shell
cd charm
```
打开configure.sh修改python配置文件位置指向python3.7.9的位置，如下

![image](https://github.com/XXXatHEU/RDSSES/assets/119908567/7f75f00c-3ec3-4f77-bf68-6bef737585d3)


```shell
sudo ./configure.sh --python=/opt/python3/python3.7.9/bin/python3.7
```

```shell
sudo make
```

```shell
sudo make install
```

### 安装pypbc

```shell
cd pypbc
```
打开pypbc.c文件，将第1338行注释掉，否则无法进行$Zr$上的除法运算
如图
![image](https://github.com/XXXatHEU/RDSSES/assets/119908567/52eecc1e-e83a-410c-a0d5-371106f448e6)

```shell
sudo python3.7 setup.py install
```

```shell
sudo pip3.7 install pypbc
```

### 后续

删除所有自己安装的gmp库

```shell
sudo rm -rf /usr/local/lib/libgmp*
```

更新动态库

```shell
sudo ldconfig
```

常用的python库安装

```shell
pip3.7 install numpy scipy pandas matplotlib pycryptodome
```
