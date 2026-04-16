import os 
from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb+srv://yourUsername:yourPassword@cluster0.mongodb.net/yourDatabaseName?retryWrites=true&w=majority")

# create database
db = client["animal_charity"]

# collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]