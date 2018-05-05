2016年12月01日 18:29:15
---
**今天遇到在requests设置移除SSL认证的时候，控制台会抛出以下警告：**

 - **问题：**

```python
C:\Python27\lib\site-packages\requests\packages\urllib3\connectionpool.py:843: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
C:\Python27\lib\site-packages\requests\packages\urllib3\connectionpool.py:843: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
登录成功
```
![这里写图片描述](http://img.blog.csdn.net/20161201182347116)


----------


> *虽然这并不影响结果的正确，但是这个提示一直存在，看着是真的别扭，尤其需要输出到报告或者是日志的时候。代码加入下面两行，取消这个警告*


----------

 - **解决：**

```python
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```


再次运行，讨厌的警告就不会出现啦，^_^。

![这里写图片描述](http://img.blog.csdn.net/20161201182538079)

----------

