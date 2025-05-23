from pymongo.collection import Collection
from extract.extract_data import create_connect_db, create_connect_collection
import pandas as pd

def visualize_collection(collection: Collection):
    for document in collection.find():
        print(document)
        
def rename_columns(collection:Collection, column_name:str, new_column_name:str) -> None:
    collection.update_many({}, {"$rename": {f'{column_name}': f'{new_column_name}'}})
    
def select_category(collection: Collection, category):
    query = {"Categoria do Produto": f'{category}'}
    books_list = list(collection.find(query))
    return books_list
        
def make_regex(collection:Collection, regex):
    query = {f'Data da Compra': {"$regex": f'{regex}'}}
    
    products_list = list(collection.find(query))
    return products_list
        
def create_dataframe(documents_list:list):
    df = pd.DataFrame(documents_list)
    return df

def rename_df_columns(df):
    df = df.rename(columns={"_id": "id",
                         "Produto": "produto",
                         "Categoria do Produto": "categoria_do_produto",
                         "Preço": "preco",
                         "Frete": "frete",
                         "Data da Compra": "data_da_compra",
                         "Vendedor": "vendedor",
                         "Local da compra": "local_da_compra",
                         "Avaliação da compra": "avaliacao_da_compra",
                         "Tipo de pagamento": "tipo_de_pagamento",
                         "Quantidade de parcelas": "quantidade_de_parcelas",
                         "Latitude": "latitude",
                         "Longitude": "longitude"
                         })
    return df

def format_date(df):
    df = df.loc[:, ~df.columns.duplicated()]
    
    df["data_da_compra"] = pd.to_datetime(df["data_da_compra"], format="%d/%m/%Y")
    df["data_da_compra"] = df["data_da_compra"].dt.strftime("%Y-%m-%d")
    
    return df
    