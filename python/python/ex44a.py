#! /usr/bin/env python
# --*-- coding:utf-8 --*--

# 继承就是用来指明一个类的大部分或全部功能都是从一个父类中获得的。
# 父类与子类有三种交互方式：
# 1.子类上的动作完全等同于父类上的动作。
# 2.子类上的动作完全覆盖了父类上的动作。
# 3.子类上的动作部分替换了父类上的动作。

# 隐式继承 implicit inheritance
class Parent(object):
	def implicit(self):
		print "PARENT implicit()"
		
class Child(Parent):
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()