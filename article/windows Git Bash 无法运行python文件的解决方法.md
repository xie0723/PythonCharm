2016年07月19日 18:21:00
---

>**今天学习Django，有一个小需求在w7 系统 的git bash 环境 运行 python 文件，但是输入命令，Enter 后，一直没任何响应，最后找到方法，总结下**

在git bash 中运行下python - -version 或 pip list 命令，都是可以正常使用。
![这里写图片描述](http://img.blog.csdn.net/20160720084415166)


但是输入python 确没有任何响应，这样的话，肯定是无法运行python文件的。
![这里写图片描述](http://img.blog.csdn.net/20160719181220644)

使用python -i   可以显示已安装python 

![这里写图片描述](http://img.blog.csdn.net/20160720174929826)

最后google 下，其实想运行python文件，很简单只需要在命令前面加上一个winpty +command 就可以了。
> 
> ![这里写图片描述](http://img.blog.csdn.net/20160725151409354)

这里我使用py -2 是因为我的电脑装了python2 和python3 ，如果你只装了一个python2或者3
直接运行就可以了。不需要加上数字2。