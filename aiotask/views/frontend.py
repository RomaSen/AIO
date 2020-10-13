import asyncio
import random

import aiohttp


async def index(request):
    return aiohttp.web.Response(text='Hello world!')


async def sum(request):
    data = request.content._buffer[0].decode('utf8').replace("'", '"').split(',')
    sum = data[0] + data[1]
    await asyncio.sleep(random.randint(0, 5))
    return aiohttp.web.Response(text=f'Sum{sum}')
