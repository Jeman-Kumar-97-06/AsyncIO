import asyncio
import time

async def fetch_data(param):
    print(f"Do Something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return("Result of {param}")

async def main():
    task1 = fetch_data(1)
    task2 = fetch_data(2)
    result1 = await task1
    print("Task 1 fully completed!")
    result2 = await task2
    print("Task 2 fully completed!")
    return [result1, result2]

t1 = time.perf_counter()

results = asyncio.run(main())

print(results)

t2 = time.perf_counter()

print(f"COmpleted in {t2-t1:.2f} seconds")