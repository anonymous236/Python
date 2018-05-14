## 系统环境
* 腾讯云服务器
* CentOS 7.4 64位 | 1核 2GB 1Mbps 系统盘：普通云硬盘

## 裸机安装说明
* 有python2.7，但没有pip:
  ```shell
  wget https://bootstrap.pypa.io/get-pip.py
  python get-pip.py
  ```
* 系统没有python3.6<br><br>
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
* pip-修改国内镜像源
  ```shell
  mkdir ~/.pip 
  vim ~/.pip/pip.conf
  [global]
  index-url = https://mirrors.aliyun.com/pypi/simple/
  ```
  阿里云 https://mirrors.aliyun.com/pypi/simple/<br>
  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/<br>
  豆瓣 http://pypi.douban.com/simple<br>
  Python官方 https://pypi.python.org/simple/<br>
  v2ex http://pypi.v2ex.com/simple/<br>
  中国科学院 http://pypi.mirrors.opencas.cn/simple/<br>
  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/<br>
* 安装CUDA [for GPU ; 云服务器应该无法安装]
  * 登录 [CUDA驱动下载](https://developer.nvidia.com/cuda-75-downloads-archive) 或复制链接 https://developer.nvidia.com/cuda-75-downloads-archive
  * 依次选择操作系统和安装包
    > 注意：<br>
      Installer Type 推荐选择 rpm（network）<br>
      network：网络安装包，安装包较小，需要在主机内联网下载实际的安装包<br>
      local：本地安装包。安装包较大，包含每一个下载安装组件的安装包<br>
      
  * 右键复制【Download】地址
  * 选择 /lib/cuda/ 目录下使用`wget`命令
  ```shell
  wget [复制的下载链接地址]
  sudo rpm -i cuda-repo-rhel7-7.5-18.x86_64.rpm(这是下载的文件)
  sudo yum clean all
  sudo yum install cuda
  ```
  * 在/usr/local/cuda-XXX/samples/1_Utilities/deviceQuery目录下，执行`make`命令，可以编译出 deviceQuery 程序

* 问题：command 'gcc' failed with exit status 1<br>
  For Redhat Versions(Centos 7) Use below command to install Python Development Package<br>
  **Python2.7**<br>
  `sudo yum install python-dev`<br>
  **Python3.6**<br>
  `sudo yum install python36-devel`<br>
