from pymongo import MongoClient
import datetime
import pprint
import copy

client = MongoClient('localhost', 27017)
db = client["FoodApp"]
collection = db["product"]
posts = collection

#insert/ add a product
def insertProduct(productName, productType, price, image):
	post = {
		"productName":productName,
		"productType":productType,
		"price":price,
		"image":image,
		"date":datetime.datetime.utcnow()}
	 '''
	 check if product is a duplicate
	 '''
	 def checkProduct(productName,price):
	 	if(pprint.pprint(posts.find_one({"productName":productName,"price":price}))):
			return True
		else:
			return False
	if heckProduct(productName,price) == False :
		post_id = posts.insert_one(post).inserted_id

		return pprint.pprint(posts.find_one({"_id": post_id}))
	else:
		return print("EXISTING PRODUCT")

def findProduct(productName,price):
	return pprint.pprint(posts.find_one({"productName":productName,"price":price}))

def changePrice(productName,price):
	old_product_doc = posts.find_one({"productName":productName,"price":price})
	new_product_doc = copy.deepcopy(old_product_doc)

	newPrice=input("New Price: ")

	new_product_doc["price"] = newPrice
	posts.update({"productName":productName}, new_product_doc, safe=True)