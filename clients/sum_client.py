import asyncio
import random
import json
import time

import aiohttp

MAX_CLIENTS = 1000
URL = 'http://0.0.0.0:5050/'


async def send_request():
    async with aiohttp.ClientSession(json_serialize=json.dumps) as session:
        payload = {
            'num1': random.randint(0, 2000),
            'num2': random.randint(0, 2000)
        }
        async with session.get(URL, params=payload) as response:
            return await response.text()

if __name__ == '__main__':
    eloop = asyncio.get_event_loop()
    start = time.time()
    tasks = [asyncio.ensure_future(send_request()) for pid in range(1, MAX_CLIENTS + 1)]
    eloop.run_until_complete(asyncio.gather(*tasks))
    print(f"Process took: {time.time() - start} seconds")
    eloop.close()
