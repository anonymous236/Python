## 系统环境
* 腾讯云服务器
* CentOS 7.4 64位 | 1核 2GB 1Mbps 系统盘：普通云硬盘

## 裸机安装说明
* 系统有python2.7，没有python3.6<br>
  安装python3.6：
  * 安装依赖环境
  ```shell
  yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
  ```
  * 安装GCC编译器环境
  ```shell
  yum -y install gcc
  ```
  * 新建目录到 /lib/python3.6/ 下(自行设定)
  * 下载Python3,解压后进入目录,编译安装
  ```shell
  wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
  tar -zxvf Python-3.6.1.tgz
  cd Python-3.6.1
  ./configure --prefix=/usr/local/python3
  make
  make install    或者 make && make install
  ```
  * 建立python3的软链
  ```shell
  ln -s /usr/local/python3/bin/python3 /usr/bin/python3
  ```
  * 将/usr/local/python3/bin加入PATH
  ```shell
  vim ~/.bash_profile
  >>> # .bash_profile
         # Get the aliases and functions
         if [ -f ~/.bashrc ]; then
                 . ~/.bashrc
         fi
         # User specific environment and startup programs
         PATH=$PATH:$HOME/bin:/usr/local/python3/bin
         export PATH
  ```
  * 保存,让上一步的修改生效并检查
  ```shell
  source ~/.bash_profile
  python3 -V
  pip3 -V
  ```
