import asyncio


async def fetch_speed(camera_id):
    sleep = 0
    speed = 0
    if camera_id == 1:
        sleep = 0.2
        speed = 48
    elif camera_id == 2:
        sleep = 2
        speed = 65
    elif camera_id == 3:
        await asyncio.sleep(0.1)
        raise ConnectionError(f"Camera {camera_id} unreachable")
    elif camera_id == 4:
        sleep = 0.4
        speed = 52

    await asyncio.sleep(sleep)

    return speed


async def process_reading(camera_id):
    try:
        speed = await asyncio.wait_for(fetch_speed(camera_id), timeout=1)
        return (camera_id, speed, None)
    except asyncio.TimeoutError:
        return (camera_id, None, "timeout")
    except ConnectionError as e:
        return (camera_id, None, str(e))


async def main():
    results = await asyncio.gather(
        process_reading(1),
        process_reading(2),
        process_reading(3),
        process_reading(4)
    )

    total_speed = 0
    success_count = 0
    for camera_id, speed, reason in results:
        if reason is None:
            print(f"Camera {camera_id}: {speed} km/h")
            total_speed += speed
            success_count += 1
        else:
            print(f"Camera {camera_id}: failed ({reason})")

    if success_count > 0:
        print(f"Average speed of {success_count} cameras is {total_speed/success_count} km/h")
    else:
        print("No successful readings, average unavailable")


asyncio.run(main())
