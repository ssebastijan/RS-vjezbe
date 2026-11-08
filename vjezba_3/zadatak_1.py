import asyncio


async def fetch_data():
    await asyncio.sleep(3)
    numbers = [i for i in range(1, 11)]
    print("Podaci dohvaćeni.")
    return numbers


async def main():
    data = await fetch_data()
    print(f"Podaci: {data}")


asyncio.run(main())
