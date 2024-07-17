import time
import asyncio


async def play_music(music: str, length: int) -> str:
    print(f"playing {music}")
    await asyncio.sleep(length)  # simulate music playing
    print(f"finished playing {music}")

    return music

async def call_api():
    print("calling api...")
    raise Exception("Error calling api") 


async def my_gather():
    start_time = time.perf_counter()
    results = await asyncio.gather(play_music("music1", 5), play_music("music2", 2))
    end_time = time.perf_counter()
    print(results)
    print(f"Total time: {end_time - start_time}")


async def my_gather_with_exception():
    results = await asyncio.gather(play_music("music1", 2), call_api(), return_exceptions=True)
    print(results)


if __name__ == "__main__":
    # asyncio.run(my_gather())
    asyncio.run(my_gather_with_exception())