import asyncio

async def func1():
    print("hi")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(func1())
loop.close()