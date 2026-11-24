import asyncio
import time


async def send_request(camera_id, duration):
    print(f"Sending request to camera {camera_id}")
    await asyncio.sleep(duration)
    print(f"Received response from camera {camera_id}")
    return camera_id


async def main():
    # Sequential
    # Ukupno trajanje je zbroj trajanja zahtjeva (3 + 1 + 2), otprilike 6 sekundi
    # odgovori stizu jedan po jedan, redom 1, 2, 3, jer svaki await ceka prethodni
    start = time.perf_counter()
    r1 = await send_request(1, 3)
    r2 = await send_request(2, 1)
    r3 = await send_request(3, 2)
    duration = time.perf_counter() - start
    print(f"Sequential: {duration:.2f} s")

    # Concurrent
    # Ukupno trajanje kao trajanje najduljeg zadatka, otprilike 3 sekunde,
    # jer se svi pokrecu u isto vrijeme
    # odgovori stizu redosljedom kojim se zavrse (2, 3, 1), a gather vraca
    # rezultate redoslijedom kojim su korutine predane ([1, 2, 3]),
    # neovisno o tome koja je prva zavrsila
    start = time.perf_counter()
    results = await asyncio.gather(
        send_request(1, 3),
        send_request(2, 1),
        send_request(3, 2),
    )
    duration = time.perf_counter() - start
    print(f"Concurrent: {duration:.2f} s")
    print(results)


asyncio.run(main())
