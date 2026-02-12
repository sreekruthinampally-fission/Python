import asyncio
import time
#to measure exec time

async def task():
    await asyncio.sleep(2)

async def main():
    start = time.perf_counter()
    #perf counter gives accurate timing

    await asyncio.gather(task(), task())
    #runs tasks concurrently

    end = time.perf_counter()
    print(f"Concurrent time: {end - start:.2f} seconds")  #total exec time

asyncio.run(main())
