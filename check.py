import asyncio

async def user_1():
    for i in range(3):
        name = input("your name: ")
        print(name)

async def display_time():
    for remaining in range(900, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_format = f'{mins:02}:{secs:02}'
        print(time_format, end='\r')
        await asyncio.sleep(1)
    print("00:00")

async def main():
    # Start the timer and display time functions
    asyncio.create_task(display_time())
    await user_1()

# Run the main function
asyncio.run(main())
