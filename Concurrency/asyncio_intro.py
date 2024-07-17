import asyncio

async def addition(n1: int, n2: int) -> int:
    outcome: int = n1 + n2
    print(outcome)


async def main():
    print('main - step 1')
    # must be awaited when calling a coroutine function within a coroutine function
    await addition(1, 2)
    print('main - step 2')


asyncio.run(main())
