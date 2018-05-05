2016年08月04日 10:37:51
---
> 选择一个合适的IDE，对于强迫症的人来说，比较重要。最开始用的是Eclipse, 之后是用Pycharm，最近发现了Atom ，推荐。
>环境： W7 ，64位  


***下载链接***
> https://atom.io/


**适合python的插件**

> ├── atom-beautify@0.29.11
├── atom-python-run@0.5.1
├── autocomplete-clang@0.9.4
├── autocomplete-modules@1.6.1
├── autocomplete-paths@1.0.2
├── autocomplete-python@1.8.6
├── block-comment-plus@0.4.0
├── build@0.65.0
├── busy@0.6.0
├── file-icons@1.7.19
├── git-plus@5.16.2
├── highlight-selected@0.11.2
├── hyperclick@0.0.37
├── language-ini@1.16.0
├── linter@1.11.16
├── linter-flake8@1.13.4
├── linter-gcc@0.6.15
├── linter-pylama@0.6.0
├── linter-python@3.0.5
├── linter-python-pep8@0.2.0
├── MagicPython@0.5.15
├── platformio-ide@1.4.0
├── platformio-ide-terminal@2.2.0
├── project-manager@2.9.7
├── python-autopep8@0.1.3
├── python-debugger@0.1.0
├── python-indent@0.4.3
├── python-isort@0.0.7
├── python-jedi@0.3.7
├── python-tools@0.6.8
├── python-yapf@0.11.0
├── script@3.9.0
├── seti-ui@1.3.2
├── terminal-plus@0.14.5
├── tool-bar@1.0.1
└── tree-view-finder@0.2.1

> 若还需要其他的插件(有插件下载排行)，请点击：[Atom 插件排行](https://atom.io/packages/list)

**插件安装**
> Aotm安装时，已经默认安装了apm包管理器，类似于Python的pip，Node.js的npm，
> 开始安装插件，建议不要在Atom 中安装，可能会一直提示失败。
> 推荐使用 ：**apm install  packageName**   
>  

> **例如   在cmd 中输入：apm  install  script**  




**运行Python文件：**
> **script插件**      是运行代码时使用，安装成功后，可以打开.py文件，快捷键ctrl+shift +b(**Mac cmd + i** )  运行python代码。


**插件升级：**
> 插件的初始安装可以使用apm install packageName 安装，之后可以在Atom的 setting→Updates 中升级.



**插件说明**
>1：这个暂时就不说了，google 下Atom + 插件名称就可以找到，例如Atom  script。
>2：安装成功以后，可能需要点击setting→package→找到对应的包名，点击setting  设置下。
>3：打开setting的方法，ctrl+shift+p 输入setting ，一般第一个，回车打开。
>4：也可以点击file→setting，如果没有主菜单，可以按照3的步骤打开setting后，找到core→
Auto Hide Menu Bar 取消√

**备注**
> 需要注意的是，yapf 需要先使用pip install  yapf 安装然后再python-yapf的 setting 中设置好path



***遇到问题***

**1：**

> 问题：突然自动补全不能使用，google也没找到答案，就一个一个的包设置。
>  解决：最后把python-jedi 禁用了，才有效，不知道什么问题，先记录下。


----------
**2：**

> 问题：提示
> ![这里写图片描述](http://img.blog.csdn.net/20160909105300958)

> 解决
>  安装
>  pip install pylama  
>  apm install linter-pylama  
>  
>  配置setting →Executeable Path   设置路径   C:/Python27/Scripts/pylama.exe

----------
**3：**
使用ctrl + alt + b 格式化代码，提示如下图
![这里写图片描述](http://img.blog.csdn.net/20171124111946071?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGllXzA3MjM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

解决:
> pip install autopep8  
> pip install isort 
>    再重启Atom

----------
**4：**
git 配置
> settings→package→搜索git plus→点击setting→找到Git path  配置自己电脑安装的git (C:\Program Files\Git\cmd\git.exe)

----------
**5：**
报错：
![这里写图片描述](https://img-blog.csdn.net/20180326171922454?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hpZV8wNzIz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

> 解决：
> pip install python-language-server

**之后会慢慢总结，再补充把**