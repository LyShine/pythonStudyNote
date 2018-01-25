import logging;
logging.basicConfig(level=logging.INFO)

# import pdb;
# 这个导入的好怪异，怎么用的，这些模块有什么用

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    # pdb.set_trace()
    # 这是得到一个类来初始化一个对象啊
    # 要根据源代码得到方法的使用？？
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
