

## 问题

使用Django，创建迁移文件的时候，提示如下报错↓：

> **python manage.py makemigrations**
>  **You are trying to add a non-nullable field 'phone' to student without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:**
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py




### 解决(models.py)：

-  方法一

```
phone = models.CharField(max_length=128, verbose_name='电话',null=True,blank=True)

```




- 方法二

```
phone = models.CharField(max_length=128, verbose_name='电话',default='blank')
```




### 区别：

设置default='blank' 时，会在前端phone 一栏，表中默认填充 blank （如下图↓）.

![这里写图片描述](https://img-blog.csdn.net/20180410131815779?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hpZV8wNzIz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)