import eksipy
import asyncio
import csv
import os


async def write_topic(topic):
    ''' Scrape the entries of given topic and saves them in a csv file '''
    eksi = eksipy.Eksi()
    topic = await eksi.getTopic(topic)
    entries = await topic.getEntrys()
    
    with open('data\\{}.csv'.format(topic), mode='w', encoding='utf-8') as topic_csv:
        writer = csv.writer(topic_csv, delimiter=',')
        for entry in entries:
            writer.writerow([entry.text()])
            
async def get_topic(topic):
    ''' Scrape the entries of the given topic and return a list of entry strings '''
    eksi = eksipy.Eksi()
    topic = await eksi.getTopic(topic)
    entries = await topic.getEntrys()
    
    return [entry.text() for entry in entries]

#loop = asyncio.get_event_loop()
#loop.run_until_complete(getTopic('php'))

def read_topic(topic):
    ''' Read a csv file of topics and return a list of entry strings '''
    with open('data\\{}.csv'.format(topic), mode='r', encoding='utf-8') as topic_csv:
        csv_reader = csv.reader(topic_csv, delimiter=',')
        return [row for row in csv_reader]
