# -*- coding: utf-8 -*-
# @Time           : 2018/11/19 下午 11:52
# @Author         : YYece
# @PROJECT_NAME   : Python-mooc-tests
# @File           : DayDayUp.py.py

def daydayup1():
    dayup = pow(1.001, 365)
    daydown = pow(0.999, 365)
    print("dayup:{:.2f}".format(dayup))
    print("daydown:{:.2f}".format(daydown))
def daydayup2():
    dayfactory = 0.005
    dayup = pow(1+dayfactory, 365)
    daydown = pow(1-dayfactory, 365)
    print("dayup:{:.2f}".format(dayup))
    print("daydown:{:.2f}".format(daydown))
daydayup2()

