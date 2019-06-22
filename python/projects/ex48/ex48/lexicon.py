#! /usr/bin/env python
# --*-- coding:utf-8 --*--

class lexicon(object):


	directions = ['north','south','east','west','down','up','left','right','back']
	verbs = ['go','stop','kill','eat']
	stops = ['the','in','of','from','at','it']
	nouns = ['door','bear','princess','cabinet']
	numbers = ['0','1','2','3','4','5','6','7','8','9']
	
	def scan(self,sentence):
		self.sentence = sentence
	
		stuff = raw_input('> ')
		words = stuff.split()	
		for word in words:
			if(directions)

	

	def convert_numbers(s):
		try:
			return int(s)
		except ValueError:
			return None
	