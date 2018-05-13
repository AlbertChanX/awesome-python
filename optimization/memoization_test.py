# coding:utf-8
# http://www.cclycs.com/s356595.html

import timeit


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


memoized_fibonacci = memoize(fibonacci)

if __name__ == '__main__':

    # 使用内置的globals()设置globals为当前全局变量集合
    # 执行次数number限制为一次
    # timeit.timeit('fibonacci(35)', globals=globals(), number=1)

    # run it in >>> 2 times
    timeit.timeit('print(memoized_fibonacci(35))', globals=globals(), number=1)
    print(timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1))
