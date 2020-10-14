import asyncio
import random
import json
import time

import aiohttp

MAX_CLIENTS = 1000
URL = 'http://0.0.0.0:5050/'


async def send_request(session, pid):
    payload = {
        'num1': random.randint(0, 2000),
        'num2': random.randint(0, 2000)
    }
    async with session.get(URL, params=payload) as response:
        response.close()


async def asynchronous_sending():
    start = time.time()

    async with aiohttp.ClientSession(json_serialize=json.dumps) as session:
        tasks = [asyncio.ensure_future(send_request(session, pid)) for pid in range(1, MAX_CLIENTS + 1)]
        await asyncio.gather(*tasks)

    print(f"Process took: {time.time() - start} seconds")


if __name__ == '__main__':
    eloop = asyncio.get_event_loop()
    eloop.run_until_complete(asynchronous_sending())
    eloop.close()
