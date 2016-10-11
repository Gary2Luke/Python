#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

path=os.getcwd()
path=path.replace('\\','/')                       #get path

def printpath(path, type):
    g = file('chuli.txt', 'w')
    out = file('output.txt', 'a')
    for fpathe, dirs, fs in os.walk(path):
        for f in fs:
            newpath = os.path.join(fpathe, f)       #traverse folder to get file's path
            g.truncate(0)                          #clear
            m = 'file %s >> chuli.txt' % newpath
            os.system(m)
            gg = file('chuli.txt', 'r')
            try:
                info = gg.readlines()[0]
                if type in info:
                    print >> out, newpath
            except:
                pass

    xxx=path.split("/")[-2] if path.split("/")[-1]==('noninteractive' or 'interactive') else path.split("/")[-1]
    print '%s %s的%s文件路径已输出到output.txt(benchmark根目录下)\n' %(xxx,type.split(' ')[0],path.split("/")[-1])

def d_or_s(path,ll):                                #static or dynamic
        if ll == 's' or ll == 'S':
            printpath(path, 'statically linked')
        elif ll == 'd' or ll == 'D':
            printpath(path, 'dynamically linked')
        elif ll == 'all':
            printpath(path, 'statically linked')
            printpath(path, 'dynamically linked')
        else:
            print '输入有误'

def maintest(chars, ll, jj):  # choose category
    global path
    path1=path
    if chars == 'l' or chars == 'L':
        path1=path1 + '/library'
    elif chars == 'm' or chars == 'M':
        path1=path1 + '/manual'
    elif chars == 'p' or chars == 'P':
        path1=path1+'/practical'
    elif chars == 's' or chars == 'S':
        path1=path1 + '/standard'
    else:
        print '输入有误'
    if jj == 'i':                              #interaction
        path1=path1+'/interactive'
    elif jj == 'n':
        path1=path1+'/noninteractive'
    elif jj == 'all':
        pass
    else:
        print '输入有误'
    d_or_s(path1, ll)

print '************benchmark************'
while(True):

    test=raw_input("**********请选择要测试的包**********\n"
                    "l代表library,m代表manual,p代表practical,s代表standard,all代表所有\n"
                     "（测试多个用'+'连接）,例如l+m,输入break退出\n ")

    if test == 'break':
        break
    out2 = file('output.txt', 'w')
    while True:
        ll = raw_input('************请选择测试静态或动态************\n'
                   's for static,d for dynamic,all for static+dynamic,输入return返回\n')
        if ll=='return':
            break
        jj = raw_input('************请选择交互或者不交互的程序************\n'
                        'i for interactive,n for noninteractive,all for interractive+noninteractive,输入return返回\n')
        if jj == 'return':
            break
        if test == 'all':
            chars = 'l+m+p+s'
        else:
            chars = test
        for i in range(0, len(chars), 2):

            maintest(chars[i], ll, jj)
        break
    break


