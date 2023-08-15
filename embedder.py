import openai

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

def embed(df):
    # Key
    openai.api_key = ""
        
    # Embedding 
    df["embedding"] = df.translation.apply(lambda x: get_embedding(x))

    return df