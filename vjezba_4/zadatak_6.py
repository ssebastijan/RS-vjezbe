import asyncio
import aiohttp


async def fetch_fact(client):
    async with client.get("https://catfact.ninja/fact") as resp:
        if resp.status != 200:
            return resp.status, None
        data = await resp.json()
        return 200, data["fact"]


async def fetch_with_retry(client, request_number, semaphore):
    delay = 0.5
    for attempt in range(1, 4):
        async with semaphore:
            try:
                status, fact = await asyncio.wait_for(fetch_fact(client), timeout=2)
            except asyncio.TimeoutError:
                status, fact = None, None
        if status == 200:
            return request_number, attempt, fact, None
        if status is not None and status != 503:
            return request_number, attempt, None, f"HTTP {status}"
        if attempt < 3:
            await asyncio.sleep(delay)
            delay *= 2

    return request_number, 3, None, "failed after 3 attempts"


async def main():
    semaphore = asyncio.Semaphore(3)
    async with aiohttp.ClientSession() as client:
        results = await asyncio.gather(
            *[fetch_with_retry(client, n, semaphore) for n in range(1, 9)]
        )

    fetched = 0
    failed = 0
    attempts_total = 0
    for request_number, attempts, fact, error in results:
        attempts_total += attempts
        if error is None:
            fetched += 1
            print(f"Request {request_number}, attempts {attempts}")
        else:
            failed += 1
            print(f"Request {request_number}, attempts {attempts}: {error}")

    print(f"Fetched: {fetched}, failed: {failed}, attempts: {attempts_total}")


asyncio.run(main())
