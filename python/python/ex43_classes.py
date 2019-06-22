#! /usr/bin/env python
# --*-- coding:utf-8 --*--

#自顶向下  因为他是从最抽象的概念（顶层）下手，一直向下做到具体的代码实现。
# 自底向上 先从代码下手，一直向上做到抽象概念
# 步骤如下
# 1.取出要解决的问题中的一小块，写些代码让它差不多能工作
# 2.细化代码让它更为正式，比如加上类和自动测试
# 3.把关键概念抽取出来然后研究他们。
# 4.把真正需要实现的东西描述出来
# 5.回去细化代码，有可能需要全部丢弃重头做起
# 6.在问题的另外一小块里重复上述流程。

from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured.Subclass it and implement enter()."
		exit(1)
		
class Engine(object):

	def __init__(self,scene_map):
		pass
		
	def play(self):
		pass
		
class Death(Scene):
	
	def enter(self):
		pass
		
class CentralCorridor(Scene):

	def enter(self):
		pass
		
class LaserWeaponArmory(Scene):

	def enter(self):
		pass
		
class TheBridge(Scene):

	def enter(self):
		pass
		
class EscapePod(Scene):
	
	def enter(self):
		pass
		
class Map(object):
	
	def __init__(self,start_scene):
		pass
		
	def next_scene(self,scene_name):
		pass
	def opening_scene(self):
		pass
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
	