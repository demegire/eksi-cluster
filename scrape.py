import eksipy
import asyncio
import os


async def getTopic():
    eksi = eksipy.Eksi()
    topic = await eksi.getTopic("php")
    entrys = await topic.getEntrys()
    for entry in entrys:
        print("*" * 10)
        print(entry.text())
        print(entry.author.nick)
        print("*" * 10)

loop = asyncio.get_event_loop()
loop.run_until_complete(getTopic())