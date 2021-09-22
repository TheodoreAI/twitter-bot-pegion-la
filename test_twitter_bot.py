import unittest, json
from twitter_bot import TwitterBot


class TestTwitterBot(unittest.TestCase):
	# Testing if the string from the word_doc is the same as the one written here.

	def test_string_status_array(self):
		obj_twitter_bot = TwitterBot()
		written_string = "Updating from a text file."
		check_string = obj_twitter_bot.get_status()
		for i in range(0, len(check_string)):
			if type(written_string) != type(check_string[i]):
				return "Not the same type"
			else:

				self.assertEqual(str(written_string), str(check_string[i]))

	# def test_get_user_tweets(self):
	# 	obj_twitter_bot = TwitterBot()
	# 	username = "a3m3a3r3i"
	# 	user = obj_twitter_bot.get_user(username)
	# 	for follower in user.followers():
	# 		print(follower.name)



	# def test_trendings(self):
	# 	obj_twitter_bot = TwitterBot()
	# 	name = "name"
	# 	trends_result = obj_twitter_bot.get_trendings()

	# 	for trend in trends_result[0]["trends"]:
	# 		print(trend[name])

	# def test_friends(self):
	# 	obj_twitter_bot = TwitterBot()
	# 	user = "a3m3a3r3i"
	# 	username = "MateoJorgeE"
	# 	print("------------")
	# 	for friend in obj_twitter_bot.get_friends(user):
	# 		print(friend.name)

	# def test_search(self):
	# 	obj = TwitterBot()
	# 	username = "MateoJorgeE"
	# 	user = obj.get_me()
	# 	ID = user.id

	# 	print(ID)
	# 	print("The searches made by me", obj.get_saved_searches(ID))

	def test_dms(self):
		obj = TwitterBot()

		get_it = obj.get_dms()
		with open("dms.txt", "w") as f:
			f.writelines(str(get_it))

		print(obj.get_dms())





if __name__ == "__main__":
	unittest.main()