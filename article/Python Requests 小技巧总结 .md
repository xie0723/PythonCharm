2016年10月11日 20:17:00
---

**关于 Python Requests ，在使用中，总结了一些小技巧把，分享下。**


----------


 **1：**保持请求之间的Cookies，我们可以这样做。

```python
import requests
self.session = requests.Session()
self.session.get(login_url) # 可以保持登录态
```
----------


**2：**请求时，会加上headers，一般我们会写成这样
 
``` python
self.session.get(url, params, headers=headers)
```
唯一不便的是之后的代码每次都需要这么写，代码显得臃肿，所以我们可以这样:

```python
#在构造函数中，这样设置是全局的。

# 设置请求头
self.s = requests.Session()
self.s.headers = {'balabala'}

# 移除服务器验证
self.s.verify = False

# 设置代理
self.s.proxies={'aa'}

# 如果后续headers有改变，再次赋值就可以了。
self.s.get(url, params, headers=new_headers)
```


----------


 **3：**默认requests请求失败后不会重试，但是我们跑case时难免遇到一些网络,服务重启，外部原因导致case失败，我们可以在Session实例上附加HTTPAdapaters 参数，增加失败重试次数。

```python
request_retry = requests.adapatrs.HTTPAdapaters(max_retries=3）

self.session.mount('https://',request_retry)  
self.session.mount('http://',request_retry)
```
这样，之后的请求，若失败，重试3次。

----------


**4：**重定向
网络请求中可能会遇到重定向，我们需要一次处理一个请求，可以把重定向禁止。

```python
self.session.post(url,data,allow_redirects=False)
```


----------


**5：** post请求提交json格式数据时(请求头为:{"Content-Type": "application/json"})，一般先要把python对象转换成json对象。可能很多时候是这样写：

```python
self.session.post(url, data=json.dumps(data))。
```
 其实post有一个默认参数json，可以直接简写成：

```
 self.session.post(url, json=data)
```




----------


**6：**写接口请求，debug时，会需要看下代码请求的详细信息，当然我们可以使用fiddler来查看，其实我们自己也可以在代码这样获取debug信息***

```python
import requests
import logging
import httplib as http_client

http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

requests.get('https://www.baidu.com')

#更好的方法是自己封装一个装饰器，就可以为任意请求函数添加一个debug功能。
```


----------


**7：**使用grequests实现异步请求。

> **pip install grequests**

```python
import grequests

urls = [
    'http://www.url1.com',
    'http://www.url2.com',
    'http://www.url3.com',
    'http://www.url4.com',
    'http://www.url5.com',
    'http://www.url6.com',
]

resp = (grequests.get(u) for u in urls)
grequests.map(resp)

# [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]

```

----------

**8：**发送自定义cookies
我们使用Session实例来保持请求之间的cookies，但是有些特殊情况，需要使用自定义的cookies
我们可以这样

```python
# 自定义cookies
cookie = {'guid':'5BF0FAB4-A7CF-463E-8C17-C1576fc7a9a8','uuid':'3ff5f4091f35a467'}

session.post('http://wikipedia.org', cookies=cookie) 

```
----------

**9：**需求确定前后端并行设计时，这时测试并没有办法调用接口，如何做接口测试呢？我们可以使用mock或者是httpretty

```python
import requests
import httpretty

# 模拟返还的状态码
@httpretty.activate
def test_beta1_access():
    httpretty.register_uri(httpretty.GET, "http://beta.com/",
                           body="here is the mocked body",
                           status=201)

    response = requests.get('http://beta.com')
    expect(response.status_code).to.equal(201)

# 模拟返还response的body
@httpretty.activate
def test_some_api():
    httpretty.register_uri(httpretty.GET, "http://beta.com/",
                           body='{"success": false}',
                           content_type='text/json')

    response = requests.get('http://beta.com/')

    expect(response.json()).to.equal({'success': False})
```
[详细使用可以查看API_DOC](https://github.com/gabrielfalcao/HTTPretty)


----------


**10：**统计一个API请求花费的时间，我们可以使用如下方法 

```python
self.session.get(url).elapsed 

```
----------

**11：**设置请求超时

```python

self.session.get(url, timeout=15)

# timeout 仅对连接过程有效，与响应体的下载无关。 
# timeout 并不是整个下载响应的时间限制，而是如果服务器在15 秒内没有应答，将会引发一个异常（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时）
```


关于Python ，requests的小技巧，就是这些。