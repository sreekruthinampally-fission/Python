#1
import asyncio
#defining async func
async def say_hello():
    print("Hello")

asyncio.run(say_hello())


#2
import asyncio 

async def wait_and_print():
    #to pause and allow othefrs to run
    await asyncio.sleep(2)
    #to run after 2 seconds
    print("Done waiting")

asyncio.run(wait_and_print())
