import eksipy
import asyncio
import csv
import os


async def getTopic(topic):
    eksi = eksipy.Eksi()
    topic = await eksi.getTopic(topic)
    entries = await topic.getEntrys()
    
    with open('{}.csv'.format(topic), mode='w', encoding='utf-8') as topic_csv:
        writer = csv.writer(topic_csv, delimiter=',')
        for entry in entries:
            writer.writerow([entry.text()])
            
    #with open('{}.csv'.format(topic), mode='r', encoding='utf-8') as topic_csv:
    #    csv_reader = csv.reader(topic_csv, delimiter=',')
    #    for row in csv_reader:
    #        print(row)


loop = asyncio.get_event_loop()
loop.run_until_complete(getTopic('php'))



