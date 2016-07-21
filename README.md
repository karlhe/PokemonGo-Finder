# Pokemon Go Notification System

This is a fork of [jxmorris12/PokemonGo-Finder](https://github.com/jxmorris12/PokemonGo-Finder), a fork of [the popular PokemonGo-Map repository](https://github.com/AHAAAAAAA/PokemonGo-Map), with the purpose of notifying users where to find nearby Pokemon. All API and map functionality was left untouched.

## Configure PushBullet
To generate a token for sending yourself notifications using the Pushbullet API, create an account on [Pushbullet](https://www.pushbullet.com/). Then click your avatar and select the "My Account" page. Scroll to where you see "Access Tokens" and click the "Create Access Token" button. Copy this hash, you'll need it later.

## Config File
Instead of from the command-line, all arguments are read from a `config.json` file.

See `config.json.sample`.

It is also recommended to use your own Google Maps API key, set it in `credentials.json`.

## Install

Must use Python 2.7 due to protobuf dependency.

Install the necessary dependencies by running `pip install --upgrade -r requirements.txt`. Create a config file and then run the main script using `python main.py`.

*Using this software is against the ToS and can get you banned. Use at your own risk.*
