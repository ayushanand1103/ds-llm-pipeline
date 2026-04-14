import pymongo
from pymongo.errors import PyMongoError
from pymongo import MongoClient
from core.config import MONGO_URI , DB_NAME

try :
    client = MongoClient(MONGO_URI)
    db = client(DB_NAME)
    client.admin.command("ping")
    print("Mongo DB connected")


except PyMongoError as e :
    print(f"Mongo DB connection failed {e}")
    raise

user_collection = db["users"]
conversations_collection = db["conversations"]
messages_collection = db["messages"]
code_excecution_collection = db["code_excecutions"]
prefference_collection = db["prefferences"]
model_version_collection = db["model_version"]



