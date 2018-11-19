# -*- coding: utf-8 -*-
# @Time           : 2018/11/17 下午 06:29
# @Author         : YYece
# @PROJECT_NAME   : Python-mooc-tests
# @File           : TempConvert.py
# @Software       : PyCharm
TempStr = input("请输入带单位的温度值")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("转换后的摄氏度为：{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后的华氏度为{:.2f}F".format(F))
else:
    print("输入格式有误")