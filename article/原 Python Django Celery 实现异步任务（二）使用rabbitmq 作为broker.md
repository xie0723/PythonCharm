2018年01月13日 13:27:07
---
之前在上一篇文章中[Python Celery 实现异步任务](http://blog.csdn.net/xie_0723/article/details/78277707)是使用Django默认作为borker （消息分发），因为升级最新的celery后，不再支持Django作为borker ，所以测试平台更换为rabbitmq  。以下简单介绍下更换的方法，其实很简单。



在django 项目下，把全局的settings.py  中修改以下代码

``` python
 # 使用rabbitmq 作为任务代理 (broker)
BROKER_URL = "amqp://" 

# 默认是以本机的mq服务作为broker。如果你需要配置成远程的mq，请填写完整的
BROKER_URL = amqp://userid:password@hostname:port/virtual_host

```

rabbitmq  的安装方法，网上有很多，请Google后安装，并且启动mq 服务。


结构图

![这里写图片描述](http://img.blog.csdn.net/20180113133441583?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGllXzA3MjM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


---
celey  结构


![这里写图片描述](http://img.blog.csdn.net/20180119131109166?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGllXzA3MjM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)