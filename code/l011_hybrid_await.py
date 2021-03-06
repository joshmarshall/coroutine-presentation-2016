import asyncio
from tornado import gen
from tornado.platform.asyncio import AsyncIOMainLoop, to_asyncio_future


async def async_timeout():
    for i in range(10, 1, -1):
        print("ASYNC TIMEOUT")
        await asyncio.sleep(i * 0.1)


async def tornado_timeout():
    for i in range(0, 10, 1):
        print("TORNADO TIMEOUT")
        await gen.sleep(i * 0.1)


def main():
    AsyncIOMainLoop().install()
    loop = asyncio.get_event_loop()

    afuture = async_timeout()
    tfuture = to_asyncio_future(tornado_timeout())

    tasks = asyncio.wait([afuture, tfuture])
    loop.run_until_complete(tasks)
    loop.close()


if __name__ == "__main__":
    main()
