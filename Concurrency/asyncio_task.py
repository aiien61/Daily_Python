import time
import asyncio

async def call_api(name: str, delay: float):
    print(f"{name} - step 1")
    await asyncio.sleep(delay)  # simulate network delay
    print(f"{name} - step 2")


async def main():
    start_time: float = time.perf_counter()

    print('start coroutine A')
    task_a = asyncio.create_task(call_api("A", 5))

    print('start coroutine B')
    task_b = asyncio.create_task(call_api("B", 2))
    
    await task_a
    print('task A done')

    await task_b
    print('task B done')

    end_time: float = time.perf_counter()
    print(f"Total time: {end_time - start_time}")


async def play_music(music: str) -> str:
    print(f"playing {music}")
    await asyncio.sleep(5)  # simulate music playing
    print(f"finished playing {music}")

    return music

async def cancel_task():
    task = asyncio.create_task(play_music("music1"))

    await asyncio.sleep(3)

    if not task.done():  # check if the task is done using .done()
        task.cancel()


async def cancel_task_with_timeout():
    task = asyncio.create_task(play_music("music2"))

    try:
        # using asyncio.wait_for to auto cancel the task if timeout
        await asyncio.wait_for(task, timeout=2)
    except asyncio.exceptions.TimeoutError:
        print("Timeout")


async def task_timeout():
    task = asyncio.create_task(play_music("music2"))

    try:
        # using asyncio.shield to not cancel the task if timeout
        await asyncio.wait_for(asyncio.shield(task), timeout=2)
    except asyncio.exceptions.TimeoutError:
        print("Timeout")
        await task

if __name__ == "__main__":
    # asyncio.run(main())
    # asyncio.run(cancel_task())
    # asyncio.run(cancel_task_with_timeout())
    asyncio.run(task_timeout())