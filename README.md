# formtest
一个学习 Django 框架的demo，方便以后自己查看。
此 demo 主要包含的知识点有:         
* 关联mysql,不要使用MysqlDB或者python-mysql这两个库，因为它们是python2.7版本下才能运行的，在python3.x下，用 pymysql 驱动,下载地址: https://github.com/PyMySQL/PyMySQL,然后在 模块的 __init__  函数中添加 import pymysql 和 pymysql.install_as_MySQLdb()
* 表单的使用，手写表单，继承自 django.forms.Form（基础窗体）和 django.forms.ModelForm（模型窗体）
* GET请求和POST请求，数据传递
* 验证码框架 captcha 的使用
