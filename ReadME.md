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
## 数据库基础使用
## Python使用MongoDB——pymongo
+ pip install pymongo
+ from pymongo import MongoClient  
  client = MongoClient("mongodb://serp:serp123456@127.0.0.1:27017")  
  db = client.venue

