#! /usr/bin/env python
# --*-- coding:utf-8 --*--

# 显式覆盖
class Parent(object):
	def override(self):
		print "PARENT override()"
		
class Child(Parent):
	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()