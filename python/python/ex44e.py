#! /usr/bin/env python
# --*-- coding:utf-8 --*--

# 方法解析顺序 Method Resolution Order MRO

# super() 和__init__搭配使用
# 最常见的super()的用法是在基类的__init__函数中使用。通常这也是唯一可以进行这种操作的地方，在这里你在子类里做一些事情，然后完成对父类的初始化。

# 合成

class Other(object):
	def override(self):
		print "OTHER override()"
		
	def implicit(self):
		print "OTHER implicit()"
		
	def altered(self):
		print "OTHER altered()"
		
class Child(object):
	
	def __init__(self):
		self.other = Other()
	
	def implicit(self):
		self.other.implicit()
		
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD,BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD,ALTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()