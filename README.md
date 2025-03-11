
# MTA API
Heads-up display for your local train station designed for terminal display or an e-paper hat running on a Raspberry Pi. This script continuously fetches and prints real-time arrival data from GTFS-RT (General Transit Feed Specification - Realtime) feeds. It retrieves data from multiple sources, formats it, and outputs it to the terminal every minute.

## Application setup

MTAPI is a python app designed to run under Python 3.3+.

##### 1. Create a `config.py` file. 
A sample is provided as `config.py.sample` in the ' `src` folder. directions are provided inside the sample file
##### 2. Set up your environment and install dependencies.  
`python3 -m venv .venv`  
`source .venv/bin/activate`  
`python3 -m pip install -r requirements.txt`

## Usage 
`python3 main.py`

## License

This project is licensed under the MIT License.

## Contributions

Feel free to contribute by submitting a pull request or report issues.