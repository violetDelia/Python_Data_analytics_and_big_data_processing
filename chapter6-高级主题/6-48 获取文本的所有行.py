# -*- coding: UTF-8 -*-

file = open("chapter6-高级主题//readme1.md", encoding='UTF-8')
'''
readlines()一次读取所有行,比较费内存
'''
for line in file.readlines():
    if "阿根廷红虾" in line or "海参" in line :
        print(line)
		
		
for line in file:
    print(line)