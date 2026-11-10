import asyncio


async def timer(name, delay):
    # Svaki poziv timer() je zasebna korutina.
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        # await asyncio.sleep(1) ne blokira thread - korutina se pauzira, event loop se budi za 1 s, u međuvremenu izvršava druge zadatke.
        await asyncio.sleep(1)
    # Petlja je gotova, korutina završava i vraća kontrolu event loopu.
    print(f'{name}: Vrijeme je isteklo!')


async def main():
    # 2. prva korutina
    # 3. create_task() rasporedjuje timer korutine u event loop.
    # 4. korutine se još ne izvršavaju, main drži kontrolu do prvog await.
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    # 5. await gather() pauzira main() i predaje kontrolu event loopu.
    await asyncio.gather(*timers)


# 1. stvara novi event loop, pokreće main() i, kad main() završi zatvara loop.
asyncio.run(main())
