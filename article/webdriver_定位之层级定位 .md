2016年01月30日 22:39:52
---
**定位目标：**
![这里写图片描述](http://img.blog.csdn.net/20160130221325276)

携程官网→如图红色框内元素
**HTML源码：**
![这里写图片描述](http://img.blog.csdn.net/20160130221747934)

**定位思路：**
一：通过classname 定位
``` python
#定位自由行
current = dr.find_elements_by_class_name("s_tab_nocurrent")
current[1].click()
```
二：通过tag定位
``` python
#先定位到父级元素searchBoxUl 
searchboxUI = dr.find_element_by_id("searchBoxUl")
#再定位子元素
boxuis = searchboxUl.find_elements_by_tag_name("li")
#定位到旅游
boxuis[3].click()
```


*当然还可以通过xpath，css等等方法，主要是为了介绍第二种分层定位的思想。在以后的工作中，可能会有很多的元素并没有规范的ID，NAME等提供。通过第二种方法，可以解决！*

``` 