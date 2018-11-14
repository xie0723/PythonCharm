# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2018/4/25 18:13'

# 1. 乘法口诀表
for m in range(1, 10):
    for n in range(1, m + 1):
        print('{}*{}={}'.format(n, m, m * n), end='\t')
    print()

# 2. 写一个匹配URL的正则表达式
import re

exp = re.compile(r'''^(https?:\/\/)?
                  ([\da-z\.-]+)
                  \.([a-z\.]{2,6})
                  ([\/\w \.-]*)\/?$
                  ''', re.X)

assert exp.match('www.google.com') is not None
assert exp.match('http://www.example/file.html') is not None
assert exp.match('https://douban.com/tag') is not None

# 3. 写一个匹配IP地址的正则表达式
exp = re.compile(r'''^(?:(?:25[0-5]
                      |2[0-4][0-9]
                      |[1]?[0-9][0-9]?)\.){3}
                      (?:25[0-5]
                      |2[0-4][0-9]
                      |[1]?[0-9][0-9]?)$''', re.X)

assert exp.match('192.168.1.1') is not None
assert exp.match('8.8.8.8') is not None
assert exp.match('256.0.0.0') is None

# 4. 把字符串 2018-01-01 用正则转化成 01/01/2018
date = '2018-01-01'
assert re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', date) == '01/01/2018'


# 5. 实现一个函数，把 CamelCase 字符串 用正则转化成 camel_case
def convert(s):
    res = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', res).lower()


assert convert('CamelCase') == 'camel_case'
assert convert('SimpleHTTPServer') == 'simple_http_server'

# 6. 在slack中，存在uid和id的对应关系，如下面的变量 ID_NAMES 。通过Slack的API能获取聊天记录，但是内容用的是uid，请用正则表达式re.sub函数实现uid和id的转换
ID_NAMES = {'U1EAT8MG9': 'xiaoming', 'U0K1MF23Z': 'laolin'}
s = '<@U1EAT8MG9>, <@U0K1MF23Z> 嗯 确实是这样的'

exp = re.compile(r'\<@.*?\>')


def id_to_name(match):
    content = match.group()
    name = ID_NAMES.get(content[2:-1])
    return '@{}'.format(name) if name else content


assert exp.sub(id_to_name, s) == '@xiaoming, @laolin 嗯 确实是这样的'

# 7. 实现Fibonacci函数
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


assert [fib(n) for n in range(16)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

# 8. 实现PYTHON版本的TREE
import os
import argparse


def tree(path, depth=1, level=0):
    items = os.listdir(path)
    
    for item in items:
        if item.startswith('.'):
            continue
        print('|   ' * level, end='')
        print('├── ', item)
        item = os.path.join(path, item)
        if os.path.isdir(item) and level < depth - 1:
            tree(item, depth=depth, level=level + 1)


# 9. 写一个装饰器inject，在__init__时自动给类注入参数
def inject(func):
    def deco(*args, **kwargs):
        args[0].__dict__.update(kwargs)
        func(*args, **kwargs)
    
    return deco


class A:
    @inject
    def __init__(self, x, y, z):
        pass


a = A(x=4, y=5, z=6)

assert a.x == 4

# 10. 使用WITH写一个函数调用计时的上下文管理器
from time import time, sleep
from contextlib import ContextDecorator


class Timed:
    def __enter__(self):
        self.start = time()
        return self
    
    def __exit__(self, type, value, traceback):
        self.end = time()
        cost = self.end - self.start
        print(f'Cost: {cost}')


class Timed2(ContextDecorator):
    def __enter__(self):
        self.start = time()
        return self
    
    def __exit__(self, type, value, traceback):
        self.end = time()
        cost = self.end - self.start
        print(f'Cost: {cost}')


with Timed():
    sleep(2)


@Timed2()
def f():
    sleep(2)


f()

# 11. 实现一个类，可以完成链式调用
from functools import reduce


class Seq:
    def __init__(self, *items):
        self.items = items
    
    def __repr__(self):
        return str(self.items)
    
    def map(self, func):
        return self._evaluate(map, func)
    
    def filter(self, func):
        return self._evaluate(filter, func)
    
    def reduce(self, func):
        return self._evaluate(reduce, func)
    
    def _evaluate(self, transform, func):
        rs = transform(func, self.items)
        if isinstance(rs, int):
            return rs
        self.items = list(rs)
        return self


# Seq(1, 2, 3, 4).map(lambda x: x * 2) == [2, 4, 6, 8]


# 12. PYTHON读取超大文件


def process():
    pass


with open("log.txt") as infile:
    for line in infile:
        process(line)

# 或者
bufsize = 65536

with open('path') as f:
    while 1:
        lines = f.readlines(bufsize)
        if not lines:
            break
        for line in lines:
            process(line)


# 13. 写一个生成素数的迭代器, 能迭代小于某数值以下的素数

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for current in range(3, int(math.sqrt(number) + 1), 2):
        if number % current == 0:
            return False
    return True


class Prime:
    def __init__(self, max):
        self.max = max
        self.number = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while 1:
            number = self.number
            if number >= self.max:
                raise StopIteration
            self.number += 1
            if is_prime(number):
                return number


assert list(Prime(30)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# 14. 写一个生成素数的生成器, 但生成一定数量之后就会停止

import math


def prime(n):
    number = 2
    while n > 0:
        if number > 2 and not number % 2:
            number += 1
            continue
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if not number % i:
                break
        else:
            yield number
            n -= 1
        number += 1


assert list(prime(5)) == [2, 3, 5, 7, 11]

# 15. 使用YIELD实现用轮转调度(ROUND-ROBIN)
from collections import deque
from itertools import cycle, islice


# https://docs.python.org/3/library/itertools.html#itertools-recipes
# 这些例子都很有用
def roundrobin(*iterables):
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


def roundrobin2(*iterables):
    num_active = len(iterables)
    q = deque(iter(it) for it in iterables)
    while q and num_active:
        try:
            t = q.popleft()
            yield next(t)
            q.append(t)
        except StopIteration:
            num_active -= 1


assert list(roundrobin('ABC', 'D', 'EF')) == ['A', 'D', 'E', 'B', 'F', 'C']
assert list(roundrobin2('ABC', 'D', 'EF')) == ['A', 'D', 'E', 'B', 'F', 'C']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='list contents of directories in a tree-like format.')
    parser.add_argument('-L', '--level', type=int,
                        help='Descend only level directories deep.')
    parser.add_argument('path', metavar='PATH', type=str,
                        help='directory path name')
    args = parser.parse_args()
    tree(args.path, depth=args.level)

# 16. 使用多线程请求一定数量HTTPBIN网站页面并存储结果
from random import uniform
from queue import Queue
from collections import defaultdict
from threading import Thread, Semaphore, current_thread

import requests

tasks_queue = Queue()
results_queue = Queue()
sema = Semaphore(3)
threads = []
results = defaultdict(list)
session = requests.Session()
URL = 'http://httpbin.org/get?a={}'


def fetch():
    while 1:
        with sema:
            if tasks_queue.empty():
                break
            value = tasks_queue.get()
            name = current_thread().name
            result = session.get(URL.format(value)).json()['args']['a']
            results_queue.put((name, result))
            sleep(uniform(0.1, 0.2))


for i in range(10):
    tasks_queue.put(i)

for i in range(5):
    t = Thread(target=fetch, name=f'Thread{i}')
    threads.append(t)
    t.start()

for t in threads:
    t.join()

while 1:
    if results_queue.empty():
        break
    name, result = results_queue.get()
    results[name].append(result)
    results_queue.task_done()

for name, values in results.items():
    print(name, values)

# 17.  使用多进程实现生产者/消费者模型，而且可以通过生产者控制消费者是否接收新的任务
from multiprocessing import Process, JoinableQueue, Event

event1 = Event()
event2 = Event()
tasks_queue = JoinableQueue()
TIMEOUT = 2

event_map = {
    0: event1,
    1: event2
    }


def producer():
    for i in range(10):
        integer = randint(10, 100)
        tasks_queue.put(integer)
        if i < 4:
            event1.set()
        else:
            event1.clear()
            event2.set()
        print(f'Produce: {integer}')
        sleep(random())
    for _ in range(len(event_map)):
        tasks_queue.put(None)
    event1.set()


def consumer(event):
    while 1:
        event_is_set = event.wait(TIMEOUT)
        if event_is_set:
            integer = tasks_queue.get()
            if integer is None:
                break
            print(f'{current_process().name}: {integer}')
            tasks_queue.task_done()


processes = []

p = Process(target=producer)
p.start()
processes.append(p)

for i in range(2):
    p = Process(target=consumer, name=f'Consumer{i}', args=(event_map.get(i),))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

# 18. 使用标准库内置模块写一个最简单的MAPREDUCE例子
# https://pymotw.com/3/multiprocessing/mapreduce.html
import codecs
import string
import collections
import itertools
from multiprocessing import current_process, Pool

with codecs.open('stopwords.txt', encoding='gbk') as f:
    STOP_WORDS = set([line.strip() for line in f])


class SimpleMapReduce:
    
    def __init__(self, map_func, reduce_func, num_workers=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = Pool(num_workers)
    
    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()
    
    def __call__(self, inputs, chunksize=1):
        map_responses = self.pool.map(
                self.map_func,
                inputs,
                chunksize=chunksize,
                )
        partitioned_data = self.partition(
                itertools.chain(*map_responses)
                )
        reduced_values = self.pool.map(
                self.reduce_func,
                partitioned_data,
                )
        return reduced_values


def file_to_words(filename):
    TR = str.maketrans({
        p: ' '
        for p in string.punctuation
        })
    
    print(f'{current_process().name} reading {filename}')
    output = []
    
    with codecs.open(filename, encoding='gbk') as f:
        for line in f:
            if line.lstrip().startswith('..') or 'http' in line:
                continue
            line = line.translate(TR)  # Strip punctuation
            for word in line.split('，'):
                word = word.lower().strip()
                if word and word not in STOP_WORDS:
                    output.append((word, 1))
    return output


def count_words(item):
    """Convert the partitioned data for a word to a
    tuple containing the word and the number of occurences.
    """
    word, occurences = item
    return (word, sum(occurences))


# 19. 使用多进程模块写一个使用优先级队列的例子

import time
from queue import PriorityQueue
from multiprocessing import Process
from multiprocessing.managers import BaseManager


class Manager(BaseManager):
    pass


Manager.register('PriorityQueue', PriorityQueue)


def double(n):
    return n * 2


def producer(q):
    count = 0
    while 1:
        if count > 5:
            break
        pri = randint(0, 100)
        print(f'put :{pri}')
        q.put((pri, double, pri))  # (priority, func, args)
        count += 1


def consumer(q):
    while 1:
        if q.empty():
            break
        pri, task, arg = q.get()
        print(f'[PRI:{pri}] {arg} * 2 = {task(arg)}')
        q.task_done()
        time.sleep(0.1)


m = Manager()
m.start()
q = m.PriorityQueue()

t = Process(target=producer, args=(q,))
t.start()
time.sleep(1)
t = Process(target=consumer, args=(q,))
t.start()
t.join()

# 20. 使用THREADPOOLEXECUTOR和多线程搭配

from time import sleep
from random import randint, random
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

NUMBERS = range(26, 32)


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def producer(futures, executor):
    for n in NUMBERS:
        r = executor.submit(fib, n)
        futures.append((r, n))


def monitor(futures):
    count = 0
    while 1:
        if count == len(NUMBERS):
            break
        for f, n in futures:
            if f.done():
                print(f'fib({n}) = {f.result()}')
                futures.remove((f, n))
                count += 1
        sleep(0.5)


threads = []
futures = []

executor = ThreadPoolExecutor(max_workers=3)
t = Thread(target=producer, args=(futures, executor))
t.start()
threads.append(t)
t = Thread(target=monitor, args=(futures,))
t.start()
threads.append(t)

for t in threads:
    t.join()


# 21. 字典值通过点号访问实现
class Dotable(dict):
    __getattr__ = dict.__getitem__
    
    def __init__(self, d):
        super().__init__(d)
        self.update(**dict((k, self.parse(v)) for k, v in d.items()))
    
    @classmethod
    def parse(cls, v):
        if isinstance(v, dict):
            return cls(v)
        elif isinstance(v, list):
            return [cls.parse(i) for i in v]
        else:
            return v


# 22. 异步生成器
import asyncio


async def fetch():
    async with ClientSession as session:
        for i in range(10):
            url = f'http://httpbin.org/get?a={i}'
            async with session.get(url) as response:
                r = await response.json()
                yield r.get('args').get('a')


async def main():
    async for rs in fetch():
        print(rs)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# 23. 写一个异步列表解析式
import asyncio
from aiohttp import ClientSession


async def fetch():
    async with ClientSession as session:
        for i in range(10):
            url = f'http://httpbin.org/get?a={i}'
            async with session.get(url) as response:
                r = await response.json()
                yield r.get('args').get('a')


async def main():
    print([rs async for rs in fetch()])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# 24 . 字典value值通过dot.号访问
class DotDict(dict):
    """
    特殊字典，通过.号访问值
    Example：
        Map = {'a': {'b': [{'c': 2},3]}}
        d = DotDict(Map)
        print(d.a.b[0]) == {'c': 2}
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    
    def __init__(self, d):
        super().__init__(d)
        self.update(**dict((k, self.parse(v)) for k, v in d.items()))
    
    @classmethod
    def parse(cls, v):
        if isinstance(v, dict):
            return cls(v)
        elif isinstance(v, list):
            return [cls.parse(i) for i in v]
        else:
            return v
    
    def __call__(self, **kwargs):
        return self.update(**dict((k, self.parse(v)) for k, v in kwargs.items()))


# 25 获取本机IP
import socket


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


#  基于时间过期的LRU缓存
from datetime import datetime, timedelta
from functools import lru_cache, wraps


def time_cached(maxsize=None, **timedelta_kwargs):
    """
    基于时间过期的LRU缓存
    `timedelta_kwargs`:
        days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0
    """
    
    def _wrapper(f):
        update_delta = timedelta(**timedelta_kwargs)
        next_update = datetime.utcnow() - update_delta
        f = lru_cache(maxsize)(f)
        
        @wraps(f)
        def _wrapped(*args, **kwargs):
            nonlocal next_update
            now = datetime.utcnow()
            if now >= next_update:
                f.cache_clear()
                next_update = now + update_delta
            return f(*args, **kwargs)
        
        return _wrapped
    
    return _wrapper


if __name__ == '__main__':
    import glob
    import operator
    
    input_files = glob.glob('novels/*.txt')
    
    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()
    
    print('\n金庸最爱说：😉\n')
    top10 = word_counts[:10]
    longest = max(len(word) for word, count in top10)
    for word, count in top10:
        print(f'{word:<{longest + 1}}: count:{count}')
