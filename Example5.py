import asyncio
import time

async def fetch_data(param):
    print(f"Do Something with {param}...")
    time.sleep(param) #---------------------------> NO AWAIT*
    print(f"Done with {param}")
    return (f"Result of {param}")

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result2 = await task1
    print("Task1 fully completed")
    result1 = await task2
    print("Task2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()
results = asyncio.run(main())
print(results)
t2 = time.perf_counter()
print(f"Completed in {t2-t1:.2f} seconds")

"""
In this case, event loop has the schedule in an order:
    task1
    task2
main() is suspended when event loop comes acroess line13
Task1 runs. Prints 'Do Something with 1...'.
Since there's no 'await', event loop waits for 1 sec, then prints 'Done with 1'.
Now the Event loop resumes main().
But, due to functions stack and FIFO principle, Since the first one in line is task2 and then 'main()', task 2 will run.
'Do Something with 2...' is printed. Timer of 2 seconds is run. Then 'Done with 2' is printed. 
Then, main() resumes,
    'Task1 fully completed' is printed
    'Task2 fully completed' is printed.
Then, results are returned.
"""