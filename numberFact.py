# Dependencies
import requests
import json

# Base URL for GET requests to retrieve number/date facts
base_url = "http://numbersapi.com/"

gameOn = "y"

while (gameOn == "y"):

	# Ask the user what kind of data they would like to search for
	type = input("what kind of data you'd like to search? [trivia, math, date, or year]: ")

	# get input number or date
	if type == 'date':
	    month = input('input month first: ')
	    day = input('input day: ')
	else:
	    number = input("what's your number? ")

	# If the kind of search is "date" take in two numbers
	# If the kind of search is anything but "date" then take one number
	if type == 'date':
	    response = requests.get(base_url + '/' + month + '/' + day + '/' + type + '?json' ).json()
	else:
	    response = requests.get(base_url + number + '/' + type + '?json').json()

	# pretty print final results
	from pprint import pprint
	pprint(response['text'])

	gameOn = input("Do you want to play one more time: (y)es or (n)o?")