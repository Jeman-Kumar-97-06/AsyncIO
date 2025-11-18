import asyncio
import time

async def fetch_data(param):
    print(f"Do Something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return (f"Result of {param}")

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Task1 fully completed")
    result2 = await task2
    print("Task2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()
results = asyncio.run(main())
print(results)
t2 = time.perf_counter()
print(f"Completed in {t2-t1:.2f} seconds")

#1. Python goes through the whole code above
#2. Its starts a event loop at line 21.
#3. main() starts running.

# THE ABOVE CODE DOES HAVE CONCURRENCY