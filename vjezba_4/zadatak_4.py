import asyncio, time

async def process_request(request_number, semaphore, stats):

    async with semaphore:
        stats["active"] += 1
        stats["max"] = max(stats["max"], stats["active"])

        await asyncio.sleep(1)

        stats["active"] -= 1

        return stats

async def main(limit):
    stats = {"active": 0, "max": 0}
    semaphore = asyncio.Semaphore(limit)

    start = time.perf_counter()
    await asyncio.gather(
        *[process_request(n, semaphore, stats) for n in range(1, 9)]
    )
    duration = time.perf_counter() - start

    print(f"Limit {limit}: max active {stats['max']}, duration {duration:.2f} s")

# Procjenjeno trajanje = ceil(requests / limit) * vrijeme izvrsenja requesta
# limit 3: ceil(8 / 3) = 3 waves * 1 s = 3 s
# limit 4: ceil(8 / 4) = 2 waves * 1 s = 2 s
asyncio.run(main(3))
asyncio.run(main(4))
