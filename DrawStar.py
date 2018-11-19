# -*- coding: utf-8 -*-
# @Time           : 2018/11/19 下午 04:21
# @Author         : YYece
# @PROJECT_NAME   : Python-mooc-tests
# @File           : DrawStar.py
import turtle as t
t.setup(800,800)
t.pencolor("yellow")
t.pensize(10)
for i in range(0,5):
    t.fd(300)
    t.right(144)
t.left(180)
for j in range(0,5):
    t.fd(300)
    t.left(144)
t.done()
