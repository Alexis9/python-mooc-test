# -*- coding: utf-8 -*-
# @Time           : 2018/11/19 上午 10:06
# @Author         : YYece
# @PROJECT_NAME   : Python-mooc-tests
# @File           : TempConvert2.py
TempStr = input()
if TempStr[0] in ['c','C']:
    F = eval(TempStr[1:]) * 1.8 + 32
    print('F{:.2f}'.format(F))
else:
    C = (eval(TempStr[1:]) - 32) / 1.8
    print('C{:.2f}'.format(C))