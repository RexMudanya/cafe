from pymongo import MongoClient
import datetime
import pprint


client = MongoClient('localhost', 27017)
db = client["FoodApp"]
collection = db["users"]
posts = collection

#add a user
def userInsert(name, email, password):
	post = {"name":name,
		"e-mail":email,
		"password":password,
		"date":datetime.datetime.utcnow()}

	'''should check if data already exists in database
		before inserting the data
	'''
	def checkData(email):
		if(pprint.pprint(posts.find_one({"e-mail":email}))):
			return True
		else:
			return False

	if checkData(email) == False :
		post_id = posts.insert_one(post).inserted_id

		return pprint.pprint(posts.find_one({"_id": post_id}))
	else:
		return print("EXISTING NAME")

#find a user
def findUser(email):
	return pprint.pprint(posts.find_one({"e-mail":email}))

#check if users credentials are valid       !!!!!!!!! NOT WORKING IN EMAIL+PWD VALIDATION
def validateUser(email, password):
	if (findUser(email)):
		return True
	else:
		return False
		#check if password is same for user e-mail in collection
	if findUser(email) == True:
		posts.find_one({"e-mail":email,"password":password})
	else:
		return print("INVALID CREDENTIALS")

#userInsert('abc','ABCD@abc.com','123456')
validateUser("ABCD@abc.com","13456")