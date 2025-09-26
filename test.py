#Asyncio is used to implement shit similar to 'async'/ 'await' in js.
#With sync-code, each line is executed if-and-only-if the previous line is done.
#So if linex takes a shit load of time, python doesn't give a fuck, linex+1 will only run after linex.
#This is not good.
#With Async-code/ Concurrent-code, u tell python: "linex takes a shit load of time, in the meantime please continue with linex+1"
#
import asyncio
import time

# print("Shit")
# async def say_hello():
#     print("hello")
#     await asyncio.sleep(2)
#     print("...world!")
# print("Fuck")

# asyncio.run(say_hello())



async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay} sec")

async def main():
    # Run tasks at the same time
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )

asyncio.run(main())
