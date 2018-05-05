2017年01月01日 22:05:00
---
环境：W7，Git2.10.2 


**问题：使用git push 代码到github上，提示**



> ssl certificate problem: unable to get local issuer certificate git push

这是因为git 提交代码时需要安全认证，可以通过以下方法设置，取消验证

**解决：**

> 找到 git的gitconfig 配置文件，如果你默认安装，路径应该在
> C:\Program Files (x86)\Git\etc\gitconfig
>notepad++ 打开后，添加下面两行

```
[http]
    sslVerify = false
    sslCAinfo = /bin/curl-ca-bundle.crt
```

保存后，再提交代码就可以了。