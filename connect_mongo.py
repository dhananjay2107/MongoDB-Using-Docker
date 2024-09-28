from pymongo import MongoClient

def connectToDB():
     username = "mongoadmin"
     password = "mongodemo"
     host = "localhost"
     port = 27017
     auth_db = "admin"
     client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_db}")
     try:
          db = client.admin
          server_status = db.command("serverStatus")
          print("Connected to MongoDB:", server_status)
     except Exception as e:
               print("Failed to connect to MongoDB:", str(e))

def main():
     #Connect to DB
     connectToDB()

if __name__ == "__main__":
      main()