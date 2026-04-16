import os 
from pymongo import MongoClient

# This line looks for the 'MONGO_URI' key you created in the Render dashboard
# If it can't find it, it will stay empty (None)
mongo_uri = os.environ.get("MONGO_URI")

# connect to MongoDB using the variable
client = MongoClient(mongo_uri)

# create database
db = client["animal_charity"]

# collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]
