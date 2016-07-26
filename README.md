# Pokemon Go Notification System

This is a fork of [jxmorris12/PokemonGo-Finder](https://github.com/jxmorris12/PokemonGo-Finder), a fork of [the popular PokemonGo-Map repository](https://github.com/AHAAAAAAA/PokemonGo-Map), with the purpose of notifying users where to find nearby Pokemon. All API and map functionality was left untouched.

This fork is focused on Slack integration, with the possibility of other integrations in the future.

## Config File
Instead of from the command-line, all arguments are read from a `config.json` file.

See `config.json.sample`.

Optional arguments:

* `step_limit`: Determines how far the "player" will search. A value of `1` is the same as a stationary player. A value of `2` means the player searches in 4 locations. And etcetera.
* `notify_distance`: Distance in meters within which to send notifications. if set to `None` will notify on everything.
* `notify_ignore`: Comma-separated list of Pokemon to not send notifications for.
* `notify_far_ignore`: If set along with `notify_distance`, will notify outside of the `notify_distance` if the Pokemon does not exist in `notify_far_ignore`. Useful for rarer pokemon.

It is also recommended to use your own Google Maps API key, set it in `credentials.json`.

See `credentials.json.sample`.

## Install

Only works with Python 2.7.

Install the necessary dependencies by running `pip install --upgrade -r requirements.txt`. Create a config file and then run the main script using `python main.py`.

*Using this software is against the ToS and can get you banned. Use at your own risk.*
