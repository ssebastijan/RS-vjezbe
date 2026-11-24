import asyncio


async def fetch_speed(attempt):
    if attempt == 1:
        await asyncio.sleep(0.8)
        return None
    elif attempt == 2:
        await asyncio.sleep(0.6)
        return None
    else:
        await asyncio.sleep(0.1)
        return 54


# Slucaj s uspjesno: 3 requesta poslana, 2 cekaju izmedju pokusaja (0.5 s, 1.0 s).
# Slucaj s grskom: 3 requesta poslana, 2 cekaju (0.5 s, 1.0 s); nakon treceg
# timeouta client odmah reporta failure, bez cekanja.
# Cekanja = requests - 1,jer nema cekanja nakon zadnjeg pokusaja.
async def fetch_with_retry():
    delay = 0.5
    for attempt in range(1, 4):
        try:
            speed = await asyncio.wait_for(fetch_speed(attempt), timeout=0.3)
            print(f"Attempt {attempt}: success, {speed} km/h")
            return speed
        except asyncio.TimeoutError:
            print(f"Attempt {attempt}: timeout")
            if attempt < 3:
                print(f"Waiting {delay} s before next attempt")
                await asyncio.sleep(delay)
                delay *= 2
    print("All attempts failed")
    return None


async def main():
    result = await fetch_with_retry()
    print(result)


asyncio.run(main())
