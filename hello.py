#!/usr/bin/env python
# print('hello world')
# name=input('please input your name:')
# print('hello,',name)
# a=100
# if a>=0:
# 	print(a)
# else:
# 	print(-a)

# birth=int(input('birth:'))

# if birth <2000:
# 	print('00 pre')
# else:
# 	print('00low')

# names=['michael','bob','tracy']
# for name in names:
# 	print(name)

# 这个居然不是随机函数
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# 什么是不可变对象 ，是对象本身不可变而不是变量不可变

# 函数的定义
# def add_num(a,b):
# 	return a+b

# print(add_num(1,2))


# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny


# 默认参数可以降低函数的调用难度
# 可以使用参数名来给函数设置参数，而不是位置参数
# 默认参数必须指向不变对象，否则多次调用，函数会记住，对象不可以，因为多次使用，指向的都是一个地址
# 可变参数，传入参数的个数是可变的 * 代表一个tuple * 还可以展开数组
# 关键字参数， 可以传入不定数量的关键字参数来调用函数，收到的是一个自动组装的dict ，标识是**
# **也可以用来解构dict ，函数中传入的dict 是其一份复制， 并不影响其本身，不知道list 是否同样
# 函数中不会改变list的指向，但是会改变list中的内容，因为函数中复制了指向的地址

# def changList(par):
	# par[1]='xxxx'
	# par=[4,5,6]

# list1=[1,2,3];
# print(list1)
# list2=changList(list1) 
# 改变了list中的数据
# print(list2)
# print(list1)

extra = {'city': 'Beijing', 'job': 'Engineer'}

def person(**kw):
    # print('name:', name, 'age:', age, 'other:', kw)
    kw['city']='nanjing'

print(extra)
person(**extra)
print(extra)
# 命名关键字参数 规定函数只能传入那些关键字参数作为参数， 使用 * 后是命名 中间是可变参数，其后面
# 的也被认为命名关键字参数
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

