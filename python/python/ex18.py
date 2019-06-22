# -*- coding: utf-8 -*-
# function 函数
# 1 它们给代码段命名，就跟变量给字符串和数命名一样。
# 2 它们可以接收参数，就跟你的脚本接收argv一样
# 3 使用#1 和 #2 ，它们可以让你创建”迷你脚本” 或者 “小命令”
# def 新建函数

# This one is like your scripts with argv
# *args :asterisk args
# def ,紧接着函数名；
# 参数必须放在圆括号()中才可以；紧接着用冒号:结束本行，然后开始下一行缩进

def print_two(*args):
	arg1,arg2 = args
	print "arg1: %r,arg2:%r" %(arg1,arg2)
	
# ok,that *args is actually pointless ,we can just do this

def print_two_again(arg1,arg2):
	print "arg1: %r,arg2: %r" %(arg1,arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():	
	print "I got nothin'."
	
print_two("zyb","zhangyb")
print_two_again("zyb","zhangyb")
print_one("First")
print_none()

	


