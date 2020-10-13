import asyncio
import random
import json
import time

import aiohttp

MAX_CLIENTS = 1000
URL = 'http://0.0.0.0:8080/sum/'


async def send_request(session, pid):
    json_data = {
        "num1": random.randint(0, 2000),
        "num2": random.randint(0, 2000)
    }
    async with session.post(URL, data=f"{random.randint(0, 100)},{random.randint(0, 100)}") as response:
        response.close()


async def asynchronous():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(send_request(session, pid)) for pid in range(1, MAX_CLIENTS + 1)]
        await asyncio.gather(*tasks)

    print(f"Process took: {time.time() - start} seconds")


if __name__ == '__main__':
    eloop = asyncio.get_event_loop()
    eloop.run_until_complete(asynchronous())
    eloop.close()
