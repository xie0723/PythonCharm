2016年05月17日 17:10:42
---




***selenium Python 总结一些工作中可能会经常使用到的API。***


- 1.**获取当前页面的Url**
```python
方法：current_url  
实例：driver.current_url
```
----------
- 2.**获取元素坐标**
```python
方法：location
解释：首先查找到你要获取元素的，然后调用location方法
实例：driver.find_element_by_xpath("xpath").location
```
----------
- 3.**表单的提交**
```python
方法：submit
解释:查找到表单（from）直接调用submit即可
实例：driver.find_element_by_id("form1").submit()
```
---
- 4.**获取CSS的属性值**
```python
方法：value_of_css_property(css_name)
实例：driver.find_element_by_css_selector("input.btn").value_of_css_property("input.btn")
```
---
- 5.**获取元素的属性值**
```python
方法：get_attribute(element_name)
实例：driver.find_element_by_id("kw").get_attribute("kw")
```
---
- 6.**判断元素是否被选中**
```python
方法：is_selected()
实例：driver.find_element_by_id("form1").is_selected()
```


----------


- 7.**返回元素的大小**
```python
方法：size
实例：driver.find_element_by_id("iptPassword").size
返回值：{'width': 250, 'height': 30}
```
---
- 8.**判断元素是否显示**
```python
方法：is_displayed()
实例：driver.find_element_by_id("iptPassword").is_displayed()
```
---
- 9.**判断元素是否被使用**
```python 
方法：is_enabled()
实例：driver.find_element_by_id("iptPassword").is_enabled()
```
---
- 10.**获取元素的文本值**
```python
方法：text
实例：driver.find_element_by_id("iptUsername").text
```
---
- 11.**元素赋值**
```python
方法：send_keys(*values)
实例：driver.find_element_by_id("iptUsername").send_keys('admin')
```
---
- 12.**返回元素的tagName**
```python
方法：tag_name
实例：driver.find_element_by_id("iptUsername").tag_name
```
---
- 13.**删除浏览器所有的cookies**
```python
方法：delete_all_cookies()
实例：driver.delete_all_cookies()
```
---
- 14.**删除指定的cookie**
```python
方法：delete_cookie(name)
实例：deriver.delete_cookie("my_cookie_name")
```
---
- 15.**关闭浏览器**
```python
方法：close()
实例：driver.close()
```
---
- 16.**关闭浏览器并且退出驱动程序**
```python
方法：quit()
实例：driver.quit()
```
---
- 17.**返回上一页**
```python
方法：back()
实例：driver.back()
```
---
- 18.**清空输入框**
```python
方法：clear()
实例：driver.clear()
```
---
- 19.**浏览器窗口最大化**
```python
方法：maximize_window()
实例：driver.maximize_window()
```
---
 - 20.**查看浏览器的名字**
```python
方法：name
实例：drvier.name
```
---
- 21.**返回当前会话中的cookies**
```python
方法：get_cookies()
实例：driver.get_cookies()
```
---
- 22.**根据cookie name 查找映射Value值**
```python
方法：driver.get_cookie(cookie_name)
实例：driver.get_cookie("NET_SessionId")
```
---
- 23.**截取当前页面**
```python
方法：get_screenshot_as_file(filename)
实例：driver.get_screenshot_as_file("D:\\Program Files\\Python27\\NM.bmp")
```
---
- 24.**获取当前窗口的坐标**
```python
方法：get_window_position()
实例：driver.get_window_position()
```
---
- 25.**获取当前窗口的长和宽**
```python
方法：get_window_size()
实例：driver.get_window_size()
```
---

 **ActionChains类鼠标操作的常用方法：**

	引入ActionChains类：from selenium.webdriver.common.action_chains import ActionChains

- 26.**右击**
``` python
方法：context_click()
实例：ActionChains(driver).context_click(driver.find_element_by_id("id")).perform()
```
---
- 27.**双击**
``` python
方法：double_click()
实例：ActionChains(driver).double_click(driver.find_element_by_name("name")).perform()
```
---
- 28：**鼠标拖放**
``` python
方法：drag_and_drop(source, target)
     source：鼠标按下的源元素；target：鼠标释放的目标元素
实例：element = driver.find_element_by_name("name")
	 target = driver.find_element_by_name("name")
     ActionChains(driver).drag_and_drop(element, target).perform()
```
---
- 29：**鼠标悬停在一个元素上（hover）**
``` python
方法：move_to_element()
实例：above = driver.find_element_by_xpath("xpath路径")
      ActionChains(driver).move_to_element(above).perform()
```
---
- 30：**按下鼠标左键在一个元素上**
``` python
方法：click_and_hold()
实例：left = driver.find_element_by_name("name")
     ActionChains(driver).click_and_hold(left).perform()
``` 

----
**键盘事件：**

	引入Keys类包：from selenium.webdriver.common.keys import Keys

---
- 31：**输入**
``` python
方法：send_keys()
实例：driver.find_element_by_id("id").send_keys("XXX")
```
---
- 32：**输入空格**
``` python
方法：send_keys(Keys.SPACE)
实例：driver.find_element_by_id("id").send_keys(Keys.SPACE)
```
---
- 33：ctrl + a
	全选输入框的内容
	ctrl + x
	剪切输入框的内容
	ctrl + v
	粘贴到输入框
	ctrl + c
	复制
``` python
方法：send_keys(Keys.CONTROL,'a')
实例：driver.find_element_by_id("id").send_keys(Keys.CONTROL,'a')
```
---
- 34：**回车代替点击**
``` python
方法：send_keys(Keys.ENTER)
实例：driver.find_element_by_id("id").send_keys(Keys.ENTER)
```
---
- 35：**制表键(Tab)**
``` python
方法：send_keys(Keys.TAB)
实例：driver.find_element_by_id("id").send_keys(Keys.TAB)
```
---
- 36：**回退键（Esc）**
``` python
方法：send_keys(Keys.ESCAPE)
实例：driver.find_element_by_id("id").send_keys(Keys.ESCAPE)
``` 

**等待时间**

> 导入 WebDriverWait 包
> from selenium.webdriver.support.ui import WebDriverWait
> 导入 time 包
>  import time

- 37：**固定等待时间**
``` python
方法：sleep()
实例：time.sleep(5)  # 等待5秒
```
---
- 38：**等待一个元素被发现，或一个命令完成，超出了设置时间则抛出异常智能等待。**
``` python
方法：implicitly_wait()
实例：driver.implicitly_wait(30)
```
---
- 39：**在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常**
``` python
"方法：WebDriverWait()"

#WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
#——driver：WebDriver的驱动程序(Ie, Firefox, Chrome或远程)
#——timeout：最长超时时间，默认以秒为单位
#——poll_frequency：休眠时间的间隔（步长）时间，默认为0.5秒
#——ignored_exceptions：超时后的异常信息，默认情况下抛NoSuchElementException异常


实例：
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("id"))


#一般由unit()或until_not()方法配合使用，同上:


调用该方法提供的驱动程序作为一个参数，直到返回值不为False。
——until(method, message=’’)

调用该方法提供的驱动程序作为一个参数，直到返回值为False。
——until_not(method, message=’’)


# 还可以与expected_conditions 一起使用
from selenium.webdriver.support import expected_conditions as EC

# 实例： 判断某个元素是否可见并且是enable的，这样才clickable

WebDriverWait(dr,15,1).until(EC.element_to_be_clickable((By.ID,"EmployeeListMenu")),"Not Find element")

```
---
- 40:**选择当前页面上所有tag**
```python
name为input的元素
inputs = driver.find_elements_by_tag_name(‘input‘)
```
---
- 41：**从中过滤出type为checkbox的元素，并勾选上**
```python
for input in inputs:
	if input.get_attribute(‘type‘) == ‘checkbox‘:
		input.click()
```
---
- 42：**使用CSS定位选择所有type为checkbox的元素，并勾选上**
```python
checkboxes = driver.find_elements_by_css_selector(‘input[type = checkbox]‘)
for checkbox in checkboxes:
    　　checkbox.click()
```
---
- 43：**把最后一个checkbox的勾去掉，pop()方法空参数时，默认移除list中的最后一个元素。**
```python
driver.find_elements_by_css_selector(‘input[type = checkbox]‘).pop().click()
```
---

**切换活动对象**

- 44：**切换浏览器handle**
```python
# 切换不同的tab页
方法：driver.switch_to.window(window_name)
# 备注：从A页跳转到B页，句柄已经切换过去，但是焦点没有切过去，所以需要switch_to.window，把焦点也切过去，才可以在当前页进行操作。
# 切换是思路，获取所有的句柄，因为返回是一个list，而且要切换的对象都是最后一个，可以使用[-1]直接切过去
# 例如：
driver.switch_to.window(driver.window_handles[-1])
```

- 45：**返回上一级表单**
```python
方法： driver.switch_to_parent_content()#旧方法
      driver.switch_to.parent_content#新方法
```
---
- 46：**返回最外层表单**
```python
方法： driver.switch_to_default_content()#旧方法
      driver.switch_to.default_content()#新方法
```
---
- 47：**切换到指定frame中**
```python
方法：driver.switch_to.frame('xxx')
实例：driver.switch_to.frame('frame_name')
     driver.switch_to.frame(index)
     driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])	      
```
---
- 48：**获取当前page的title**
```python
方法：driver.title
实例：driver.title
      
```
---
- 49：**焦点切换到弹窗。**
```python
方法：driver.switch_to_alert()
实例：driver.switch_to_alert()
      
```

---
- 50：**前进**
```python
方法：
driver.forward()   
```
---

- 51：**刷新页面**
```python
方法：driver.refresh() 
```
---

      

***暂时总结这么多，如有遗漏，会再补充。***