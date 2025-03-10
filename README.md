
## Running the server

MTAPI is a Flask app designed to run under Python 3.3+.

1. Create a `settings.cfg` file. A sample is provided as `settings.cfg.sample`. #TODO
2. Set up your environment and install dependencies.  
`$ python3 -m venv .venv`  
`$ source .venv/bin/activate`  
`$ python3 -m pip install -r requirements.txt`
3. Run the server  
`$ python3 main.py`


[stop id here](https://data.ny.gov/Transportation/MTA-Subway-Stations/39hk-dx4f/explore/query/SELECT%0A%20%20%60gtfs_stop_id%60%2C%0A%20%20%60station_id%60%2C%0A%20%20%60complex_id%60%2C%0A%20%20%60division%60%2C%0A%20%20%60line%60%2C%0A%20%20%60stop_name%60%2C%0A%20%20%60borough%60%2C%0A%20%20%60cbd%60%2C%0A%20%20%60daytime_routes%60%2C%0A%20%20%60structure%60%2C%0A%20%20%60gtfs_latitude%60%2C%0A%20%20%60gtfs_longitude%60%2C%0A%20%20%60north_direction_label%60%2C%0A%20%20%60south_direction_label%60%2C%0A%20%20%60ada%60%2C%0A%20%20%60ada_northbound%60%2C%0A%20%20%60ada_southbound%60%2C%0A%20%20%60ada_notes%60%2C%0A%20%20%60georeference%60%0AWHERE%20caseless_one_of%28%60stop_name%60%2C%20%22Myrtle%20Av%22%29%0AORDER%20BY%20%60station_id%60%20ASC%20NULL%20LAST/page/filter)