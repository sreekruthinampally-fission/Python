import asyncio
import time

async def blocking():
    time.sleep(2)  # Blocks entire event loop
    print("Blocking finished")

async def non_blocking():
    await asyncio.sleep(2)  # Does not block
    print("Non-blocking finished")

async def main():
    #runs concurrently
    await asyncio.gather(blocking(), non_blocking())

asyncio.run(main())
