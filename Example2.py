import asyncio
import time

async def fetch_data(param):
    print(f"Do Something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return(f"Result of {param}")

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

# 1. Py goes through the whole code above.
# 2. It starts a event loop at line 21. 
# 3. main() starts running. 
# 4. fetch_data(1) returns a pending coroutine object. fetch_data isn't executed yet.
# 5. fetch_data(2) returns a pending coroutine object. fetch_data isn't executed yet.
# 6. when py sees 'result1 = await task1'. This is when python suspends main() function. ie., pauses it.
# 7. fetch_data(1) starts running. 
# 8. Inside the fetch_data(1), it first prints 'Do something with 1...'.
# 9. Then, py comes across the await keyword again inside the fetch_data(1) function. Now, the event loop suspends the fetch_data(1) execution
# 10.Now py waits for 1 sec [cuz param is 1].
# 11.After 1 second, fetch_data(1) continues to work. 'Done with 1' is printed and 'Result of 1' is returned from fetch_data(1) and assigned to result1.
# 12.Now main() continues to run and 'Task 1 fully completed!' is printed.
# and so on....

# THE ABOVE CODE DOES NOT HAVE CONCURRENCY
