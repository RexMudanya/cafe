from pymongo import MongoClient
import datetime
import pprint
import copy

client = MongoClient('localhost', 27017)
db = client["FoodApp"]
collection = db["Transaction"]
posts = collection

#new transaction (inhouse)

#new transaction (inhouse)

#aggregation of all transactions on date

#aggregation of all transactions on a product

#aggregation of all transactions on a location