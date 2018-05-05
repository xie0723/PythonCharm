2016年08月29日 12:30:31
---
.**描述**
> 业务有一个发货流程，人工操作太过于繁琐，所以想通过代码实现。首先遇到问题是在Windows上与linux服务器交互，使用SFTP协议（SSL加密的FTP协议，类似于HTTPS。PS：个人理解！）上传下载文件


**安装**

> pip install paramiko            



**代码demo**                                

----------

```python
import paramiko

host = "123.123.123.123"
port = 54321
user = "XXX"
password = "XXXX"


# 第一种登录服务器的方法
def login_sftp1():
	try:
		# 建立连接管道
		t = paramiko.Transport((host,port))# 注意是双层括号，之前搞了好久。
		# 建立连接
		t.connect(username=user,password=password)
		# 实例化一个clint对象，并通过ssh transport操作文件
		sftp = paramiko.SFTPClient.from_transport(t)
	except Exception as e:
		print (e)
    # 查看目标服务器的当前文件夹的目录文件,默认参数path='.'。
	print sftp.listdir()
	t.close()
	sftp.close()
	
# 第二种登录方法
def login_sftp2()
	try:
		sc= paramiko.SSHClient()
		sc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		sc.connect(host,port,user,password)
		# 获取操作文件的实例也有两种方式 
		sftp = paramiko.SFTPClient.from_transport(sc.get_transport())#①
		-------------------------------------------------------------------
		sftp = ssh.open_sftp()#②
	except Exception as e:
		print (e)
	print sftp.listdir()
	sc.close()
	sftp.close()
----------
# 文件上传
sftp.put(localpath,remotepath)

#文件下载
sftp.get(remotepath,localpath)
```

