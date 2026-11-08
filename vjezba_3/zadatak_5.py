import asyncio


async def secure_data(card_data: dict):
    await asyncio.sleep(3)

    return {
        "last_name": card_data['last_name'],
        "card_number": abs(hash(card_data['card_number'])),
        "cvv": abs(hash(card_data['cvv']))
    }

async def main():

    cards = [
        {
            "last_name": "Doe",
            "card_number": "HR123456487970155",
            "cvv": "1234"
        },
        {
            "last_name": "Mova",
            "card_number": "HR189564187461651",
            "cvv": "8612"
        },
        {
            "last_name": "Guzina",
            "card_number": "HR148965141554615",
            "cvv": "1986"
        }
    ]

    tasks = [asyncio.create_task(secure_data(n)) for n in cards]
    results = await asyncio.gather(*tasks)

    for r in results: print(f"Last name: {r['last_name']}, card_number: {r['card_number']}, cvv: {r['cvv']}")


asyncio.run(main())
