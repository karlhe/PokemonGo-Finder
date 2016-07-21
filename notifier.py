import json
from geopy.geocoders import Nominatim
from datetime import datetime
import requests

# Initialize object
def init():
	# global pushbullet_client, wanted_pokemon
	global slack_key, slack_channel
	# load pushbullet key
	with open('config.json') as data_file:
		data = json.load(data_file)

		# get slack details
		slack_key = _str( data["slack_key"] )
		slack_channel = _str( data["slack_channel"] )


# Safely parse incoming strings to unicode
def _str(s):
  return s.encode('utf-8').strip()

# Notify user for discovered Pokemon
def pokemon_found(pokemon):
	# get name
	pokename = _str(pokemon["name"]).lower()

	# get address
	coords = "{}, {}".format(str(pokemon["lat"]), str(pokemon["lng"]))
	location = Nominatim().reverse(coords)
	# Truncate the address
	address = ",".join(location.address.split(",")[0:2])

	# Locate pokemon on GMAPS
	gMaps = "http://maps.google.com/maps?q={},{}&24z".format(str(pokemon["lat"]), str(pokemon["lng"]))

	# Get disappearance time
	disappear_time = str(datetime.fromtimestamp(pokemon["disappear_time"]).strftime("%I:%M%p").lstrip('0'))

	# Create notification
	notification_text = "*{}* is here until *{}* at *{}* ({})".format(_str(pokemon["name"]), disappear_time, address, gMaps)

	# Post to Slack
	post_url = "https://slack.com/api/chat.postMessage"
	post_params = { "token": slack_key, "as_user": "true", "channel": slack_channel, "text": notification_text }
	response = requests.post(post_url, data=post_params)

init()
