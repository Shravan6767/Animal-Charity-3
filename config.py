import os 
from pymongo import MongoClient

# This pulls the real string (with your real password) from Render's settings
mongo_uri = os.environ.get("MONGO_URI")

# Connect using the variable, not a hardcoded string
client = MongoClient(mongo_uri)

# Create database
db = client["animal_charity"]

# Collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]
