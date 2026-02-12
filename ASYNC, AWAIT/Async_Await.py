import asyncio

async def task1():
    await asyncio.sleep(1)
    #to wait one second and print
    print("Task 1 done")

async def task2():
    await asyncio.sleep(2)
    #to wait two seconds and print
    print("Task 2 done")

async def main():
    await task1()
    #task1 to finish first
    await task2()
    #task2 to finsih first

asyncio.run(main())
