import asyncio
import time

#Normal Function:
def sync_function(test_param: str) -> str:
    print("This is a sync function")     #Prints 'This is a sync function'. It blocks the next line till then.
    time.sleep(0.1)                      #Function sleeps for 0.1 sec. It blocks the next line till then.
    return f"Sync Result : {test_param}" #Returns 'Sync Result : {__parameter__}'

#Async Co-Routine Function:
async def async_function(test_param:str) -> str:
    print("This is an async co routine function") 
    await asyncio.sleep(0.1)
    return f"Async Result : {test_param}"

async def main():
    #------------------------------------------------------------------
    sync_result = sync_function("Jack")
    print(sync_result)
    #Output :
    #  This is a sync function
    #  Sync Result: Test
    
    
    #------------------------------------------------------------------
    #Returns Future Object: The below code block is where the programmer creates a loop, tells python when to start, run and stop manually
    loop = asyncio.get_running_loop()
    future = loop.create_future()  # A Promise like Object
    print(f"Empty Future : {future}")  
    
    future.set_result("Future Result: Test")
    future_result = await future
    print(future_result)
    #Output:
    #  Empty Future : <Future pending>
    #  Future Result: Test
    
    
    #-------------------------------------------------------------------
    #Returns a Coroutine Object:
    coroutine_obj = async_function("Test") #This 'async_function("Test")' immediately returns a 'pending object'
    print(coroutine_obj)
    
    coroutine_result = await coroutine_obj #This is where shit actually happens --> This line actually runs the 'async_function()'
    print(coroutine_result)
    #Output:
    #	<coroutine object async_function at 0x74134451d480>
    #	This is an async co routine function
    #	Async Result : Test
    
    
    #-----------------------------------------------------------------
    #Creating a Task :
    task = asyncio.create_task(async_function("Test"))
    #async_function is wrapped with 'create_task' and given to the event loop. Unlike the 'manual', 'create_running_loop', you give event loop the control
    print(task)
    #Output:
    #	<Task pending name='Task-2' coro=<async_function() running at /Users/Jeman/Documents/AsyncIO/withoutAsyncIO.py:10>>
    #	This is a async co routine function
    #	Async Result : Test
    
    
if __name__ == "__main__":
    asyncio.run(main())