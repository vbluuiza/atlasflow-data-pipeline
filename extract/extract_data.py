from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.database import Database
from pymongo.collection import Collection
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

def connect_mongo() -> MongoClient:
    
    uri = os.getenv('mongo_uri')
    if not uri:
        raise ValueError("'mongo_uri' environment variable not found")

    client = MongoClient(uri, server_api=ServerApi('1'))
    
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        raise

def create_connect_db(client:MongoClient, db_name:str):
    db = client[db_name]
    return db

def create_connect_collection(db: Database, col_name:str) -> Collection:
    return db[col_name]

def extract_api_data(url:str):
    response = requests.get(url)
    return response.json()

