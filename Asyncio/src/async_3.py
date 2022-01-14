import asyncio

async def make_americano():
    print("Ame Start")
    await asyncio.sleep(3)
    print("Ame End")
    return "Americano"
    
async def make_latte():
    print("Latte start")
    await asyncio.sleep(5)
    print("Latte end")
    return "Latee"
    
async def main():
    a = make_americano()
    b = make_latte()
    
    result = await asyncio.gather(a, b)
    
    print(result)
    
print("Main Start")
asyncio.run(main())
print("Main End")