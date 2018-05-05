> 在此记录下，之前没有遇到过类似问题，都是使用的常规的send_keys()方法，模拟的ctrl+a  这种组合键等，单独操作键盘总结下。

```python
# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = "2016/5/19 18:46"

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
builder = ActionChains(driver)
builder.key_down(Keys.F12).perform()
sleep(5)
driver.quit()

```


![这里写图片描述](http://img.blog.csdn.net/20160519190610320)