"""
This module provides functions to connect to MongoDB, create a database,
insert documents, and fetch documents from the database.
"""
from pymongo import MongoClient
import pymongo

def connect_to_db(username, password, host, port, auth_db):
    """Connect to MongoDB and return the client instance."""
    try:
        mongo_client = MongoClient(
            f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_db}"
        )
        return mongo_client
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB:", e)
        return None

def create_and_insert(mongo_client, db_name, collection_name, document):
    """Create a database and collection, then insert a document."""
    try:

        db = mongo_client[db_name]
        collection = db[collection_name]
        inserted_id = collection.insert_one(document).inserted_id
        print(f"Inserted document ID: {inserted_id}")
    except pymongo.errors.PyMongoError as e:
        print("Error during insert operation:", e)

def fetch_documents(mongo_client, db_name, collection_name):
    """Fetch all documents from a specified collection."""
    try:
        db = mongo_client[db_name]
        collection = db[collection_name]
        all_docs = collection.find()
        for doc in all_docs:
            print(doc)
    except pymongo.errors.PyMongoError as e:
        print("Error fetching documents:", e)

if __name__ == "__main__":
    USERNAME = "mongoadmin"
    PASSWORD = "mongodemo"
    HOST = "localhost"
    PORT = 27017
    AUTH_DB = "admin"

    client = connect_to_db(USERNAME, PASSWORD, HOST, PORT, AUTH_DB)
    if client:
        document = {"name": "John", "age": 29, "city": "Kochi"}
        create_and_insert(client, "mydatabase", "mycollection", document)
        fetch_documents(client, "mydatabase", "mycollection")

    client.close()
