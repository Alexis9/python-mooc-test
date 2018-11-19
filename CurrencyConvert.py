# -*- coding: utf-8 -*-
# @Time           : 2018/11/19 上午 10:17
# @Author         : YYece
# @PROJECT_NAME   : Python-mooc-tests
# @File           : CurrencyConvert.py
Currency = input()
if Currency[0:3] == "RMB":
    USD = eval(Currency[3:]) / 6.78
    print("USD{:.2f}".format(USD))
elif Currency[0:3] == "USD":
    RMB = eval(Currency[3:]) * 6.78
    print("RMB{:.2f}".format(RMB))