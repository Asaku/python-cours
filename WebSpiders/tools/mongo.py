from pymongo import MongoClient
import datetime

class Db:
	def __init__(self):
		self.client = MongoClient('localhost', 27017)
		self.db = self.client.spider

	def insertEmail(self, newEmail):
		try:
			post = {"email": newEmail, "date": datetime.datetime.utcnow()}
			posts = self.db.posts
			post_id = posts.insert_one(post).inserted_id
		except:
			print ("Already in the database")
