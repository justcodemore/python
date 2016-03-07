# __author__ = 'admin'
# -*- coding: utf-8 -*-

import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
tasts = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasts))
loop.close()
