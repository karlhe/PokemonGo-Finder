import json
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from datetime import datetime
import requests

class Notifier:

	def __init__(self, origin, debug):
		self.debug = debug

		with open('config.json') as data_file:
			data = json.load(data_file)

		# get slack details
		self.slack_key = self.str(data["slack_key"])
		self.slack_channel = self.str(data["slack_channel"])

		if data["notify_ignore"]:
			self.notify_ignore = [pokemon.lower().strip() for pokemon in data["notify_ignore"].split(',')]

		if data["notify_distance"]:
			self.notify_distance = int(data["notify_distance"])

		# Set origin point to calculate distance from
		self.origin = origin

	# Safely parse incoming strings to unicode
	@staticmethod
	def str(s):
		return s.encode('utf-8').strip()

	# Approximates distance from origin
	def distance(self, point):
		dist = vincenty(self.origin, point).meters
		self.debug("Distance is {}m.".format(int(dist)))
		return dist

	# Notify user for discovered Pokemon
	def pokemon_found(self, pokemon):
		pokename = self.str(pokemon["name"])
		pokeid = str(pokemon["id"])

		# Don't notify if on ignore list
		if self.notify_ignore:
			if pokename.lower() in self.notify_ignore or pokeid in self.notify_ignore:
				self.debug("Ignored {}.".format(pokename))
				return

		# Don't notify if outside distance limit
		coordinates = (pokemon["lat"], pokemon["lng"])
		if self.notify_distance:
			if self.distance(coordinates) > self.notify_distance:
				self.debug("Pokemon {} was too far away.".format(pokename))
				return

		# We're good to notify!
		self.debug("Notifying {}:{}.".format(pokeid, pokename))

		# Get address
		location = Nominatim().reverse("{}, {}".format(str(coordinates[0]), str(coordinates[1])))
		# Truncate the address
		address = ",".join(location.address.split(",")[0:2])

		# Locate pokemon on GMAPS
		maps_link = "http://maps.google.com/maps?q={},{}&20z".format(str(coordinates[0]), str(coordinates[1]))

		# Get disappearance time
		disappear_time = str(datetime.fromtimestamp(pokemon["disappear_time"]).strftime("%I:%M%p").lstrip('0'))

		# Create notification
		notification_text = "*{}* is here until *{}* at *{}* ({})".format(pokename, disappear_time, address, maps_link)

		# Post to Slack
		post_url = "https://slack.com/api/chat.postMessage"
		post_params = { "token": self.slack_key, "as_user": "true", "channel": self.slack_channel, "text": notification_text }
		response = requests.post(post_url, data=post_params)
