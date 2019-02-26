from pymongo import MongoClient
import datetime
import pprint

client = MongoClient('localhost', 27017)
db = client["FoodApp"]
collection = db["users"]

def userInsert(name, password):
	post = {"name":name,
		"password":password,
		"date":datetime.datetime.utcnow()}

	posts = db.post
	'''should check if data already exists in database
		before inserting the data
	'''
	def checkData(name):
		if(pprint.pprint(posts.find_one({"name":name}))):
			return True
		else:
			return False

	if checkData(name) == False :
		post_id = posts.insert_one(post).inserted_id

		return pprint.pprint(posts.find_one({"_id": post_id}))
	else:
		return print("EXISTING NAME")

def findUser(name):
	posts=db.post
	return pprint.pprint(posts.find_one({"name":name}))

def validateUser(name, password):
	if (findUser(name)):
		return True
	else:
		return False
		#check if password is same for user in collection
	if findUser(name) == True:
		posts=db.post
		posts.find_one({"name":name,"password":password})


#userInsert('mike','123456')
findUser('mike')
validateUser('mike','123456')