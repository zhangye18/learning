# -*- coding: utf-8 -*-
# varible exercise
# 字符串和文本

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = " Those who know %s and those who %s."  % (binary,do_not)
print x
print y
 
print " I said : %r." % y
print " I alse said :'%s'." % y
 
hilareious = False
joke_evaluation = " Isn't that joke so funny ?! % r "
 
print joke_evaluation % hilareious
 
w = " This is the left side of ..."
e = " a string with a right side."

print w + e 