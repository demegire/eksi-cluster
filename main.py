import asyncio
import pandas as pd

from scrape import get_topic
from translate import translate
from embedder import embedderEksi

async def main():
    
    #loop = asyncio.get_event_loop()
    odtu = await get_topic('odtu')
    df = pd.DataFrame(odtu, columns = ['entries'] )
    df['translation'] = df['entries']
    for i in range(len(df)):
        df.iloc[i, 1] = translate(df.iloc[i,0])
    print(df)
    df = embedderEksi(df)
    #print(df.iloc[2,2])
    
    return df

loop = asyncio.get_event_loop()
loop.run_until_complete(main())