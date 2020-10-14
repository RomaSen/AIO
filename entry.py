import aiohttp
import asyncio
import uvloop

from aiotask import create_app

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = create_app()

if __name__ == '__main__':
    aiohttp.web.run_app(app, port=5050)
