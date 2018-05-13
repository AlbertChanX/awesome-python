# -*- coding:utf-8 -*-

# 装饰器     myfunc传入 @deco
# def deco(func):
#     def warpper(*args, **kwargs):
#         print('start')
#         func(*args, **kwargs)
#         print('end')
#     return warpper

# @deco
# def myfunc(parameter):
#     print("run with %s" % parameter)

# myfunc("something")

# Python中有三种方法，实例方法、类方法(@classmethod)、静态方法(@staticmethod)
# 类方法和静态方法皆可以访问类的静态变量(类变量)，但不能访问实例变量


class A(object):
    var = 1  # 类的静态变量(类变量)

    def __init__(self):
        self.name = 'leon'  # 实例变量

    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print self.name  # 访问实例变量
        print('self:', self)

    @classmethod
    def class_foo(cls, x):  # 类方法，第一个参数为类本身
        print("executing class_foo(%s,%s)" % (cls, x))
        cls.static_foo(1)  # 使用类参数调用静态方法
        print('cls:', cls)

    @staticmethod
    def static_foo(x):  # 为静态方法，可以不接收参数
        print("executing static_foo(%s)" % x)


a = A()
print a.var
print(a.foo(1))
print(a.class_foo(1))
A.static_foo(1)  # 直接调用静态方法

# 闭包，延迟求值
# def delay_fun(x, y):
#     def caculator():
#         return x+y
#     return caculator

# print('返回一个求和的函数，并不求和')
# msum = delay_fun(3,4)
# print('调用并求和:')
# print(msum())

# class Apple(object):
#     name = 'apple'  #类变量

# p1 = Apple()
# p2 = Apple()
# p1.nam = 'orange'  #类变量在class外定义
# print(p1.nam)
# print(p2.name)

'''迭代器'''

# for x in iter((1, 2, 3, 4, 5)):
#     print(x)

# '''生成器  生成器是包含有__iter__()和__next__()方法的'''
# def myyield(n):
#     while n>0:
#         print("开始生成...:")
#         yield n           #如果没有return，则默认执行到函数完毕时返回StopIteration；==continue,break
#         #return
#         print("完成一次...:")
#         n -= 1
# for i in myyield(4):
#     print(u"遍历得到的值:",i)
