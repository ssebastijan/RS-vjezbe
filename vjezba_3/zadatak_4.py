import asyncio, random

async def check_parity(number: int):
    await asyncio.sleep(2)

    if number % 2:
        return f"Broj {number} je neparan."
    else:
        return f"Broj {number} je paran."

def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(10)]


async def main():
    random_numbers = generate_random_numbers()

    tasks = [asyncio.create_task(check_parity(n)) for n in random_numbers]
    results = await asyncio.gather(*tasks)

    for r in results: print(r)


asyncio.run(main())
