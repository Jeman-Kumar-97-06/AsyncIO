import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(),count(),count())

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    main()  
    elapsed = time.perf_counter()-start
    