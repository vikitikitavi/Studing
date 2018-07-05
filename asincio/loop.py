import asyncio


async def task_gen(identity, loop):
    await asyncio.sleep(1)
    print(identity)
    loop.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete([task_gen(1, loop), task_gen(3, loop)])
loop.close()
