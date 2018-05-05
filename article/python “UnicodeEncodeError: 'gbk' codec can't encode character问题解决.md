2017年03月02日 16:58:45
---
 - 环境
> OS:w7
> PY:python3.5
> IDE:Pycharm
> moudle：requests

 - 问题
 报错内容：
![这里写图片描述](http://img.blog.csdn.net/20170302161518401?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGllXzA3MjM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
> 在爬取网页内容存储在txt文档时，遇到一个问题，google了好久，都没有解决。不得不说，编码的问题，真是个头疼的问题（尤其是使用py2，更是痛苦）

 - 分析
> 一般遇到编码问题
> 
> ①：例如A转成Ｂ，若A不是unicode类型，先decode成unicode，然后再转成B类型，unicode就像一个桥梁。
> 
> ②：但还有一个情况是，虽然Ａ是unicode类型，但是因为A数据中包含一些特殊符号，例如→，把这个符号编码为GBK的时候，不识别，就会报以上错误。
> 
> 存到本地txt的时候，在w7系统中，新建的文件默认编码为：gbk。就会出现第二种情况。


 -  解决方法

```python
	with open(filepath, 'a+',encoding='utf-8') as fp #因为utf-8编码是可变长编码，可以识别任何的字符，所以就不会出现以上错误了。
```

