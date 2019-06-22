# -*- coding: utf-8 -*-

#print 后面加逗号（，），print就不会输出换行符而结束这一行跑到下一行
print "How  old are you ?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much dou weight?",
weight = raw_input()

print "So,you're %r old ,%r tall and %r heavy." %(age,height,weight)