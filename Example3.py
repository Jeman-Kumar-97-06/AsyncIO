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
#4. As soom as Event loop comes across 'task1 = async.create_task(fetch_data(1))', It schedules the task.
#5. As soom as Event loop comes across 'task2 = async.create_task(fetch_data(2))', It schedules the task.
#6. When it reaches 'result1 = await task1', it suspends 'main()' function and starts the execution of fetch_data(1) via task1.
#7. It first prints 'Do Something with 1...'.
#8. When it reaches the line 'await asyncio.sleep(1)' inside the fetch_data(1) function, it suspends 'fetch_data(1)'
#9. The timer of 1 sec is started in the background i/o
#10.Now Event Loop sees if there are any other tasks in the schedule. It sees 'task2' in the schedule and stars its execution.
#11.Now it prints 'Do Something with 2...'.
#12.When it reaches the line 'await asyncio.sleep(2)' inside the fetch_data(2) function, it suspends 'fetch_data(2)'
#13.The timer of 2 sec is started in the background i/o
#14.The concurrency part of this code are those timers. They are running concurrently.
#15.As soon as 1 sec is finished. 'fetch_data(1)' continues to run, prints 'Done with 1' and returns 'Result of 1' which is assigned to 'result1'.
#   'Task1 fully completed' will be printed.
#16.In the remaining 1 sec, the times of 2 sec will be done. 'fetch_data(2)' continues to run, prints 'Done with 2' and returns 'Result of 2' which is assigned to 'result2'.
#   'Task2 fully completed' will be printed.
#17.The whole program finishes in 2 secs due to concurrency.


# THE ABOVE CODE DOES HAVE CONCURRENCY