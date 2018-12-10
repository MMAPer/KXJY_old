# 项目环境
## 虚拟环境——windows:virtualenvwrapper
+ 安装：在已有python3.6解释器的前提下。
比如本人是在conda的python36虚拟环境下：
pip install virtualenvwrapper-win
Linxu系统中使用：pip install virtualenvwrapper
+ 优点：
比起virtualenv，可以统一管理，方便切换环境  
比起conda，环境更纯净、简洁
+ 使用：
    - （1）配置WORKON_HOME环境变量，指定虚拟环境存储目录
    - （2）创建虚拟环境：
    mkvirtualenv -p D:\Anaconda3\envs\python36\python.exe kjjy
    - （3）查看已安装的虚拟环境：
    lsvirtualenv
    - （4）启动虚拟环境：workon kjjy
    - （5）退出虚拟环境：deactivate
    - （6）删除虚拟环境：rmvirtualenv kjjy

## Django环境——Django2.0
+ （1）切换环境：workon kjjy
+ （2）安装Django：  
    pip install django==2.0  
+ （3）在项目工程目录下创建项目：  
    cd E:\djangoPro  
    django-admin startproject kjjy
+ （5）创建app：  
    cd kjjy  
    python manage.py startapp venue
+ （4）运行：  
  settings.py的ALLOWED_HOSTS里面加入自己电脑的ip  
  python manage.py runserver 0.0.0.0:8000  
  实现局域网内电脑访问
  
# 项目结构介绍
+ （1）manage.py：以后和项目交互基本上都是基于这个文件，一般都是在终端输入python manage.py [子命令]。  
可以输入python manage.py help看下能做什么事情。除非你知道自己在做什么，  
一般情况下不应该编辑这个文件
+ （2）settings.py：本项目的配置项，以后所有和项目相关的配置都是放在这个里面
+ （3）urls.py：这个文件是用来配置URL路由的，比如访问http://127.0.0.1:8000/news  
是访问新闻列表页
+ （4）wsgi.py：项目与WSGI协议兼容的web服务器入口，部署的时候需要用到，  
一般情况下不需要修改


# 数据库——MongoDB
## 安装
+ 官网下载MongoDB4.0及以上版本
+ 安装，中间过程将MongoDB安装为服务，然后取消勾选MongoDB compass
+ 安装过程中会出现服务启动失败，选择Ignore。
+ Ignore掉，然后在安装目录bin文件夹下找到mongod.cfg文件，  
  把最后一行的mp:删除掉，再手动重启服务即可。  
  （关闭服务是：net stop MongoDB）
+ 如果需要自己再重新指定数据目录和日志文件呢？比如：
1.在安装目录data文件夹下创建下的文件夹db，用来保存具体的数据库，  
在log文件夹下创建新文件mongo.log；
2.打开命令行，cd到安装目录的bin文件夹下，  
输入命令mongod --dbpath D:\MongoDB\Server\4.0\data\db   
--logpath D:\MongoDB\Server\4.0\log\mongo.log --logappend
+ 可能遇见的错误：
  - (1)提示“服务没有响应控制” 造成错误的原因是在第一步配置时，输入有误。在 cmd 中 使用 sc delete MongoDB 命令来删除之前安装的服务，并重新执行第一步并确保准确无误。
  - (2)报错“拒绝访问”，  
2016-11-01T20:52:21.647+0800 I CONTROL [main] Trying to install Windows service ‘MongoDB’  
2016-11-01T20:52:21.648+0800 I CONTROL [main] Error connecting to the Service Control Manager: 拒绝访问。  
原因是没有以管理员身份运行 cmd  
  - （3）net start MongoDB报错：发生服务特定错误：1000  
有人说，先删除服务，在建服务，试了，对我没用。  
简单点，直接进入db文件夹，先删除 mongod.lock 文件，然后重新启动服务即可；  
要是还不行，就继续删 storage.bson文件，然后问题就解决了~

## 使用
+ 1.添加你安装MongoDB的bin目录到环境变量中的path：比如我的D:\MongoDB\bin  
cmd打开控制台，然后输入mongo回车，可以进入MongoDB的shell中，  
输入show dbs可以看到数据库。表示装成功；  
+ 2.赋予用户访问权限  
MongoDB 默认直接连接，无须身份验证，如果当前机器可以公网访问，且不注意Mongodb 端口（默认 27017）的开放状态，那么Mongodb就会产生安全风险，被利用此配置漏洞，入侵数据库。  
解决方案：
  - 【1】禁止公网访问MongoDB端口  
  网络配置：由于网络配置因人而异，需要根据自己实际环境进行配置，不作冗述。  
  大致可以从以下方面禁止：在路由器中关闭端口转发；防火墙iptables禁止访问。  
  在外网机器命令中运行：telnet your.machine.open.ip 27017  
  - 【2】见word文档吧（有截图）。暂不提供，内部享用

## Python使用MongoDB——pymongo
+ pip install pymongo
+ from pymongo import MongoClient  
  client = MongoClient("mongodb://serp:serp123456@127.0.0.1:27017")  
  db = client.venue

