# -*- coding: utf-8 -*-
# http://blog.konghy.cn/2016/04/20/python-cache/
# https://www.jianshu.com/p/f7258e266cc6
import datetime
import random
from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


@lru_cache()
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_fast(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a


class MyCache:
    """"""

    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 10

    def __contains__(self, key):
        """
        根据该键是否存在于缓存当中返回True或者False
        """
        return key in self.cache

    def update(self, key, value):
        """
        更新该缓存字典，您可选择性删除最早条目
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()
        self.cache[key] = {'date_accessed': datetime.datetime.now(),
                           'value': value}

    def remove_oldest(self):
        """
        删除具备最早访问日期的输入数据
        """
        oldest_entry = None

        for key in self.cache:
            if oldest_entry == None:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry]['date_accessed']:
                oldest_entry = key

        self.cache.pop(oldest_entry)

    @property
    def size(self):
        """
        返回缓存容量大小
        """
        return len(self.cache)


if __name__ == '__main__':
    # cache test
    keys = ['test', 'red', 'fox', 'fence', 'junk',
            'other', 'alpha', 'bravo', 'cal', 'devo', 'ele']
    s = 'abcdefghijklmnop'
    cache = MyCache()
    for i, key in enumerate(keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(s) for i in range(20)])
            cache.update(key, value)
        print("#%s iterations, #%s cached entries" % (i + 1, cache.size))

    print(add(1, 2))
    print(add(1, 2))
    print(add(2, 3))
