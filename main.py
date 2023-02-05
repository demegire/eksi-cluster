import asyncio

from scrape import get_topic
from translate import translate

async def main():

	#loop = asyncio.get_event_loop()
	odtu = await get_topic('odtu')
	print(translate(odtu[0]))
	
	

loop = asyncio.get_event_loop()
loop.run_until_complete(main())