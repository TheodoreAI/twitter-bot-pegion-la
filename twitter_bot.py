# You are going to need the dependencies in the requirements file.
# You are also going to to make an .env file to safely store your apps keys. 
# Or you can use environment variables.

import tweepy
import sys
from dotenv import dotenv_values 



#  Make sure that your modules are imported:

dotenv = 'dotenv'
if dotenv not in sys.modules:
	print("You have not imported the {} module".format(dotenv))
	# import env variables
config = dotenv_values(".env")


# Authenticate to your Twitter
auth = tweepy.OAuthHandler(config["CONSUMER_KEY"], config["CONSUMER_SECRET"])
auth.set_access_token(config["ACCESS_TOKEN"], config["ACCESS_TOKEN_SECRET"])

# Create API object

api_object = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

"""The API methods can be grouped into the following categories:
timelines, tweets, users, followers, methods 
for own account, likes, blocking users, searches, trends, stremaing: https://tweepy.readthedocs.io/en/latest/api.html"""




# To get info of a specific person on the twitter home timeline


class TwitterBot:
	"""
		The real coding begins.

	"""
	def __init__(self):
		self.str_status_array = []

	def get_timeline(self):
		# Makes a status update from this function
		# To get the info from your home timeline:

		# timeline = api_object.home_timeline()
		# for twt in timeline:
		# 	print(f"{twt.user.name} said {twt.text}")

		pass

	def add_status(self, text):
		# Reads the text from a .txt file in the root directory.
		with open('word_doc_txt.txt') as f:
			lines = f.readlines()
			self.str_status_array.append(lines)
			return lines



# To send a tweet using the update_status method

# api_object.update_status("tweeting from a text editor")
make_twt_bot = TwitterBot()
sent_text = TwitterBot.add_status()
print(sent_text)






