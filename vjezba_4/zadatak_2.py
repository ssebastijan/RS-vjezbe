import asyncio
import aiohttp


async def fetch_fact(client, request_number):
    async with client.get("https://catfact.ninja/fact") as resp:
        if resp.status != 200:
            raise RuntimeError(f"Request {request_number} failed with HTTP {resp.status}")
        else:
            data = await resp.json()
            print(f"Received response for request {request_number}")
            return (request_number, data['fact'], data['length'])


async def main():
    async with aiohttp.ClientSession() as client:

        results = await asyncio.gather(
                fetch_fact(client, 1),
                fetch_fact(client, 2),
                fetch_fact(client, 3),
                fetch_fact(client, 4),
                fetch_fact(client, 5),
            )
        request_number, fact, length = max(results, key=lambda r: r[2])
        print(f"Longest fact ({length} characters, request {request_number}): {fact}")


asyncio.run(main())
