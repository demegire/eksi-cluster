import eksipy
import asyncio
import pandas as pd

async def write_topic(topic,start_page,end_page):
    eksi = eksipy.Eksi()
    topic = await eksi.getTopic(topic)
    df = pd.DataFrame(columns=['entry'])
    for page in range(start_page,end_page+1):
        entries = await topic.getEntrys(page)
        for entry in entries:
            df = df.append({'entry':entry.text()},ignore_index=True)
    df.to_csv('data/{}.csv'.format(topic),index=False,encoding='utf-8')

async def get_topic(topic,start_page,end_page):
    eksi = eksipy.Eksi()
    topic = await eksi.getTopic(topic)
    df = pd.DataFrame(columns=['entry'])
    for page in range(start_page,end_page+1):
        entries = await topic.getEntrys(page)
        for entry in entries:
            df = df.append({'entry':entry.text()},ignore_index=True)
    return df

# asyncio.run(write_topic("php",1,10))