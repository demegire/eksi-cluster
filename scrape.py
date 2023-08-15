import eksipy
import pandas as pd

async def get_topic(topic_name, start_page, end_page):
    
    eksi = eksipy.Eksi()
    eksi.eksi = "https://eksisozluk1923.com/"
    topic = await eksi.getTopic(topic_name)

    all_entries = []
    for page in range(start_page, end_page + 1):
        entries = await topic.getEntrys(page)
        for entry in entries:
            all_entries.append(entry.text())

    df = pd.DataFrame(all_entries, columns=['entry'])

    return df