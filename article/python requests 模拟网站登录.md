2016年07月27日 18:27:06
---

**目的**
> 最近一直在做接口自动化的工作，有些接口的调用，必须先拥有登录态，所以开始模拟登陆把。

**环境**
> OS:w7
> 
> IDE:Pycharm
> 
> 使用Python 的requests 模块
> 安装：pip install requests 
> 
> Requests中文DOC：[API说明](http://docs.python-requests.org/zh_CN/latest/)


----------

**过程**

*模拟登录个人理解：接口层直接操作的模拟登录，本质上与UI层登录是相同的，都是把需要验证的数据，提交给服务器对应的函数作验证。（urls→views→Model→DB），所以我们要做的就是把人工post的数据，使用代码提交。*


----------


> - 模拟的前提首先需要找到登录接口,可以在登陆的时候，输入错误的账号密码，找到对应的API。
> 
> - 然后抓包看post了哪些数据，一般post过去的数据dict格式。
> 
> - 可以使用抓包工具查看，用fiddler或者Firefox，Chrome自带的开发者工具（F12），我用的是Chrome。
> 
> 下图为登陆提交的数据：
> ![登录提交的数据](http://img.blog.csdn.net/20160727181350524)



----------
**分析POST数据**

> - user：登录用户名。
> 
> - pass：登录密码。
> 
> - captcha：验证码。可以看到默认值是空(默认值为空的参数，一般在后端函数中是有默认值。)
> 
> - chkRememberMe：登录的时候，勾选自动登录，True代表下次打开网页自动登录，False 相反。 
> - csrf_token：因为csrf_token每次请求时是变化的，所以需要使用requests的Session方法构造一个session实例 带着之前的csrf_token 进行登录验证（csrf_token是服务器给访问网站的用户一个ID标识）。
> - referer：告诉服务器是从什么地方过来的，（可以在正常登录的时候，获取该值.）
> - deviceId：访问时的设备编号（可以在正常登录的时候，获取该值）

----------


> CSRF_TOKEN：这个字段，单独拿出来说明。
> 作用：为了防止CSRF攻击，详细请看：[CSRF攻击](http://www.cnblogs.com/hyddd/archive/2009/04/09/1432744.html)  

>获取： 
>**我们可以通过首次访问首页，获取CSRF_TOKEN，**然后带着获取的值，访问登录页。 

> PS(一般token获取，打开首页的时候，服务器返回的一个认证字段，这个token值可能会存在返回的html 中，也可能在cookies或者返回的json中，具体视情况获取)

*我们的网站是通过这个URL获取token 值*
```python
self.url_open = 'https://passport.beta1.fn/gateway/login'
```

----------


**代码demo**

```python

# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2016/7/27 16:51'

import requests
import json


class loginFN(object):
	"""
	构造请求数据
	"""

	def __init__(self):
		self.url_open = 'https://passport.beta1.fn/gateway/login'
		self.url_login = 'https://passport.beta1.fn/login/clogin'
		
		self.s = requests.Session()
		
		# 加headers 伪造请求头。
		self.s.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/51.0.2704.103 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest',
		}
		# 取消安全认证
		self.s.verify = False
	
	def get_csrf_token(self):
		"""
		因为登录时需要先获取csrfToken值，所以先get获取，
		然后在下方post数据的时候使用。
		:return: csrfToken
		"""
		page = self.s.get(self.url_open)
		csrfToken = page.cookies['CSRF_TOKEN']
		return csrfToken

	def login_fn(self):
		csrfToken = self.get_csrf_token()
		form_data = {
			'user': 'tester001@163.com',
			'pass': 'xie0723',
			'captcha': '',
			'chkRememberMe': 'true',
			'referer': 'aHR0cHM6Ly9ob21lLmJldGExLmZuL21lbWJlci9ob21l',
			'CSRF_TOKEN': csrfToken,
			'deviceId': '801142e17bf4ecc19cbbb32b22eec213',
		}
		req = self.s.post(self.url_login, data=form_data)
		res = json.loads(req.content)  # 把json 对象转换成python对象
		assert res['ret'] == 200  # 开发自定义的一个status,登录成功就返还ret 200
		print (req.content)


if __name__ == '__main__':
	loginFN().login_fn()

```

**改进的地方**

> 还有很多可以添加的，像如何抓包，如何看post的数据，如果查看requests 报文和response报文等等，网上有很多。


**总结**

> 一直想模拟网站登录，在网上查了好多的资料，一直没有成功过。后面就暂时放下了，中间学了很多理论的东西，像《图解HTTP》《HTTP权威指南》，熟悉了requests+json 等。知识是慢慢积累的，不可能一次性就搞明白。
> 





