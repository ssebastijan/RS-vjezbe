import asyncio, time

async def get_users():
    await asyncio.sleep(3)
    return [{"id": 1, "name": "Ana"}, {"id": 2, "name": "Marko"}]

async def get_products():
    await asyncio.sleep(5)
    return [{"id": 1, "name": "Mouse"}, {"id": 2, "name": "Tablet"}]


async def main():

    start = time.perf_counter()

    users, products = await asyncio.gather(
        get_users(),
        get_products()
    )

    duration = time.perf_counter() - start


    print(users)
    print(products)
    print(f"Trajanje: {duration}")


asyncio.run(main())
