
from pymongo.collection import Collection
import pandas as pd

def insert_data(collection: Collection, data:list) -> int:
    if not isinstance(data,list):
        data = [data]
        
    result = collection.insert_many(data)
    return len(result.inserted_ids)


def save_csv(df, path):
    df.to_csv(path, index=False)
    print(f'Dataframe saved in {path}')