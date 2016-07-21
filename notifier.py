import json
from pushbullet import Pushbullet
from geopy.geocoders import Nominatim
from datetime import datetime
import time
import requests

pushbullet_client = None
wanted_pokemon = None

# Initialize object
def init():
	# global pushbullet_client, wanted_pokemon
	global slack_key, slack_channel
	# load pushbullet key
	with open('config.json') as data_file:
		data = json.load(data_file)
		# get list of pokemon to send notifications for
		# wanted_pokemon = _str( data["notify"] ) . split(",")
		# transform to lowercase
		# wanted_pokemon = [a.lower() for a in wanted_pokemon]
		# get api key
		# api_key = _str( data["pushbullet"] )
		# pushbullet_client = Pushbullet(api_key)
		slack_key = _str( data["slack_key"] )
		slack_channel = _str( data["slack_channel"] )


# Safely parse incoming strings to unicode
def _str(s):
  return s.encode('utf-8').strip()
  # return s.strip()

# Notify user for discovered Pokemon
def pokemon_found(pokemon):
	# get name
	pokename = _str( pokemon["name"] ).lower()
	# check array
	# if not pokename in wanted_pokemon: return
	# notify
	# address = Nominatim().reverse(str(pokemon["lat"])+", "+str(pokemon["lng"])).address
	coords = "{}, {}".format(str(pokemon["lat"]), str(pokemon["lng"]))
	address = Nominatim().reverse(coords).address
	# Locate pokemon on GMAPS
	gMaps = "http://maps.google.com/maps?q={},{}&24z".format(str(pokemon["lat"]), str(pokemon["lng"]))
	notification_text = "Pokemon Finder found {}!".format(_str(pokemon["name"]))
	disappear_time = pokemon["disappear_time"]
	disappear_time = str(datetime.fromtimestamp(pokemon["disappear_time"]).strftime("%I:%M%p").lstrip('0'))
	# location_text = "Go search at this location: " + address + ". Locate on Google Maps : " + gMaps + ". " + _str(pokemon["name"]) + " will be available until " + disappear_time + "."
	location_text = "Go search at this location: {}. Locate on Google Maps : {}. {} will be available until {}.".format(address, gMaps, _str(pokemon["name"]), disappear_time)
	# push = pushbullet_client.push_note(notification_text, location_text)
	print(notification_text)
	print(location_text)
	slack_text = "{} {}".format(notification_text, location_text)
	post_url = "https://slack.com/api/chat.postMessage"
	post_params = {
		"token": slack_key,
		"channel": slack_channel,
		"text": slack_text
	}
	response = requests.post(post_url, data=post_params)
	print(response)
	print(response.content)

init()
