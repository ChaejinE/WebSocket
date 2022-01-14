import asyncio

async def make_americano():
    print("Ame Start")
    await asyncio.sleep(3)
    print("Ame End")
    
async def make_latte():
    print("Latte start")
    await asyncio.sleep(5)
    print("Latte end")
    
async def main():
    a = make_americano()
    b = make_latte()
    
    await asyncio.gather(a, b)
    
print("Main Start")
asyncio.run(main())
print("Main End")