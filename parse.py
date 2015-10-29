import json
from pprint import pprint

with open('bought_a_car_100.json') as df:
	data = json.load(df)

print len(data['statuses'])

user_text = {}

for tweet in data['statuses']:
	text = tweet['text']
	if text.startswith('RT'):
		continue
	user = tweet['user']['screen_name']
	user_text[user] = text

for user, text in user_text.items():
	print "[" + user + "]   ", text