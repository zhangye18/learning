# -*- coding: utf-8 -*-

# 参数 argument , 参数变量 argument variable Argv 
# 解包 unpack : 把Argv中的东西解包，将所有的参数一次赋值给左边的这些变量

# 将Python 特性引入脚本的方法，模块 module：这些导入（import）的特性,库 library
from sys import argv

script,first,second,third = argv

print "The script is called:",script
print "Your first varible is :",first
print "Your second varible is :",second
print "Your third varible is :",third
