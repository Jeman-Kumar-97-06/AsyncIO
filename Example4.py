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
    result2 = await task2
    print("Task2 fully completed")
    result1 = await task1
    print("Task1 fully completed")
    return [result1, result2]


t1 = time.perf_counter()
results = asyncio.run(main())
print(results)
t2 = time.perf_counter()
print(f"Completed in {t2-t1:.2f} seconds")

"""
In the above code, The order of schedule is the same inside event loop:
    task1
    task2

when main() is suspended.
    Event loop starts task1 and starts timer of 1 sec in bg i/o and fetch_data(1) is suspended
    Event loop in mean time also starts timer of 2 sec in bg i/o and fetch_data(2) is suspended

As 1 sec timer completes first, fetch_data(1) resumes,
    'Done with 1' is printed. Then the return value 'Result of 1' is saved in memory.
As 2 sec timer completes second, fetch_data(2) resumes,
    'Done with 2' is printed. Then the return value 'Result of 2' is saved in memory.

Then main() resumes.
    'Task2 fully completed' is printed. Then,
    'Task1 fully completed' is printed. Then,
    results are returned.

"""