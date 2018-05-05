2016年03月08日 10:37:40
---
***使用Python ，HTMLTestRunner 生成测试报告时，遇到很奇怪的问题，明明运行的结果，没有任何报错，就是不生成测试报告，纠结好久。google+baidu搜索结果也不满意，最后终于解决，先总结下。***


 **代码示例**
 Login.py
```python

"""

OS:W7 64位
IDE：Pycharm
Py：Python2.7.11

"""
# -*- coding: utf-8 -*-
__Author__ = "xiewm"

import time
from selenium import webdriver
import HTMLTestRunner
import unittest
from PO_login import LoginPage

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.username = 'xxxxx'
        self.password = 'xxxxx'

    def test_user_login(self):
        driver = self.driver
        username = self.username
        password = self.password
        login_page = LoginPage(driver)
        login_page.open()
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.submit()
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login('test_user_login'))
    filename = 'E:\\testresult.html'

    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
        runner.run(suite)

```

 **解决方法**

 1： filename = 'E:\\testresult.html’，如果是在windows环境，文件名要使用以下几种格式。

```
 ①filename = 'E:\\testresult.html’ 
 ②filename = r'E:\testresult.html'  
 ③filename = 'E:/testresult.html'  
```
---
  2：若不是使用with做文件的上下文管理，记得要`fp.close()` 关闭打开的文件，才可以保存。
```python
fp = open(filename, 'wb')
fp.close()
```
---
3：第三种就奇葩了，看截图（截图为同一代码）（Pycharm IDE）
图一
![这里写图片描述](http://img.blog.csdn.net/20160308103336051)

图二
![这里写图片描述](http://img.blog.csdn.net/20160308103350774)

*如果是以图一方式运行，就不会有报告生成，至于原因,可能是因为if __name__ == '__main__'。的原因*

---

> 2016年11月25日09:01:08，大概知道什么原因了，因为Pycharm 自带测试框架，在右上角，![这里写图片描述](http://img.blog.csdn.net/20161229160025817?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGllXzA3MjM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   点击Edit Configurations→Python tests→选中你要删除的项目![这里写图片描述](http://img.blog.csdn.net/20161229160336537?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGllXzA3MjM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)删除，这样就不会自动执行unittest。

---


4：又遇到一种情况，按照以上3个方法都不行，使用快捷键:Ctrl+shift+F10  还是无法生成report，最后在pycharm的右上角，发现了一个按钮(shift + F9)如图
![这里写图片描述](http://img.blog.csdn.net/20160510162834853)
这样就可以运行了，⊙﹏⊙b汗。（前提是必须在Edit Configurations 中配置好，你需要运行的.py   Script  Path 的文件路径）

如下图配置。

![这里写图片描述](http://img.blog.csdn.net/20180113130807651?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGllXzA3MjM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


---
5:又遇到无法生成测试报告的问题了，按照之前总结的各种方法还是不行，最后，原来就仅仅修改一行代码就可以 了，在此记录下。

```python

#原 if __name__ == '__main__':
if __name__ == 'interface_demo':
# 把main修改成自己的文件夹名就可以了
至于if__name__ == '__main__'  的作用，google下。
```

------


6： 如果还是不行的话，换个IDE(例如Atom Eclipse )  or  直接在cmd 中运行
		   > python  Login.py 

**就总结这么多。以上几种方法应该可以解决大部分的问题，如果有遇到其他的情况，也会继续总结**





  
 

