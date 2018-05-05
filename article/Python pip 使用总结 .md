2016年07月25日 16:52:56
---
 1. pip install package #安装包
> pip install selenium

 1. pip install -v package==version #安装指定版本号的包
> pip install -v selenium==2.53.6

 1. pip uninstall package #卸载
> pip uninstall selenium

 1. pip list # 显示当前环境安装的所有包

 1. pip download #下载包
> 


 1. pip freeze # 显示当前环境安装的所有包
> 这pip list 和pip freeze命令输出差不多，但是格式有些区别
> pip list       显示的格式是 ：selenium(2.53.6)
> pip freeze 显示的格式是：selenium==2.53.6

 1. pip show package # 显示包的详细信息
 
> **pip show selenium** 

> Metadata-Version: 2.0
Name: selenium
Version: 2.53.6
Summary: Python bindings for Selenium
Home-page: https://github.com/SeleniumHQ/selenium/
Author: UNKNOWN
Author-email: UNKNOWN
Installer: pip
License: UNKNOWN
Location: c:\python27\lib\site-packages
Requires:
Classifiers:
  Development Status :: 5 - Production/Stable
  Intended Audience :: Developers
  License :: OSI Approved :: Apache Software License
  Operating System :: POSIX
  Operating System :: Microsoft :: Windows
  Operating System :: MacOS :: MacOS X
  Topic :: Software Development :: Testing
  Topic :: Software Development :: Libraries
  Programming Language :: Python
  Programming Language :: Python :: 2.6
  Programming Language :: Python :: 2.7
  Programming Language :: Python :: 3.2
  Programming Language :: Python :: 3.3
  Programming Language :: Python :: 3.4
  
8 .  pip search package #查找包
> pip search  selenium  查找pypi所有包含selenium 关键字的包，例如pytest-selenium