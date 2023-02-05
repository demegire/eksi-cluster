import pandas as pd
import tiktoken
import openai
import os
import numpy as np
from openai.embeddings_utils import get_embedding

def embedderEksi(df):
    # keys
    openai.organization = ""
    openai.api_key = ""
    
    # embedding model parameters
    embedding_model = "text-embedding-ada-002"
    embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
    max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191
    
    # embedding 
    df["embedding"] = df.translation.apply(lambda x: get_embedding(x, engine=embedding_model))

    return df