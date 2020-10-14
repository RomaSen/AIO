import asyncio
import random
import json

from aiohttp import web


class SummatorView(web.View):

    async def get(self):
        summ = int(self.request.query['num1']) + int(self.request.query['num2'])
        response_obj = {'sum': summ}
        await asyncio.sleep(random.randint(0, 5))
        return web.Response(text=json.dumps(response_obj), status=200)
