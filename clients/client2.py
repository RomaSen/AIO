import random
import time

import aiohttp
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


loop = asyncio.get_event_loop()
start = time.time()
coroutines = [get(f"http://0.0.0.0:5050/?num1={random.randint(0, 2000)}&num2={random.randint(0, 2000)}") for _ in range(1000)]
results = loop.run_until_complete(asyncio.gather(*coroutines))
print(f"Process took: {time.time() - start} seconds")
