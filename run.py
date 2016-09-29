#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
def staticpath(path):
    for fpathe, dirs, fs in os.walk(path):
        for f in fs:
            if '_static' in f:
                print os.path.join(fpathe, f)

def dynamicpath(path):
    for fpathe, dirs, fs in os.walk(path):
        for f in fs:
            if '_dynamic' in f:
                print os.path.join(fpathe, f)

path=os.getcwd()
path=path.replace('\\','/')
print '************benchmark************'
while(True):

    test=raw_input("**********请选择要测试的包（l代表library,m代表manual,p代表practical，s代表stadard,输入break退出)**********\n ")

    if test=='l' or test=='L':
        while (True):
            ll=raw_input('************请选择测试静态或动态(s for static,d for dynamic,输入return返回上一层）************\n')
            if ll=='s'or ll=='S':
                for filename in os.listdir(path+'/library/static'):
                    print os.path.abspath(filename)

            elif ll=='d' or ll=='D':
                for filename in os.listdir(path+'/library/dynamic'):
                    print os.path.abspath(filename)
            elif ll == 'return':
                break
            else:
                print '输入有误'

    elif test=='m' or test=='M':
        while (True):
            mm=raw_input('************请选择测试静态或动态(s for static,d for dynamic,,输入return返回上一层）************\n')
            if mm=='s'or mm=='S':
                staticpath(path+'manual')
            elif mm=='d' or mm=='D':
                dynamicpath(path + 'manual')
            elif mm == 'return':
                break
            else:
                print '输入有误'

    elif test=='p' or test=='P':
       print '测试集为空'

    elif test=='s' or test=='S':
        while(True):
            ss=raw_input('************请选择测试静态或动态(s for static,d for dynamic,输入return返回上一层）************\n')
            if ss=='s'or ss=='S':
                showpath(path + 'standard')

            elif ss=='d' or ss=='D':
                showpath(path + 'standard')
            elif ss=='return':
                break
            else:
                print '输入有误'

    elif test=='break':
        break
    else:
        print '输入有误'
