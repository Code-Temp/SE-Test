import asyncio

async def main():
    a = 1
    print("hello")
    await asyncio.sleep(1)
    print("world")

if __name__ == "__main__":
    asyncio.run(main())