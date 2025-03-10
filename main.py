import requests
import time
from google.transit import gtfs_realtime_pb2
from config import FEED_URL, STOP_IDS, TIME_RANGE

def fetch_gtfs_rt():
    """Fetch GTFS-RT data from the feed URL."""
    response = requests.get(FEED_URL)
    if response.status_code == 200:
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)
        return feed
    else:
        print("Error fetching GTFS-RT data:", response.status_code)
        return None

def parse_gtfs_rt():
    """Parse GTFS-RT feed and filter by stop ID and arrival time."""
    feed = fetch_gtfs_rt()
    if not feed:
        return

    current_time = int(time.time())  # Get current time in epoch seconds

    for entity in feed.entity:
        if entity.HasField("trip_update"):
            for stop_time_update in entity.trip_update.stop_time_update:
                if stop_time_update.stop_id in STOP_IDS and stop_time_update.HasField("arrival"):
                    arrival_time = stop_time_update.arrival.time

                    if current_time <= arrival_time <= current_time + TIME_RANGE:
                        print(f"Upcoming arrival at stop {stop_time_update.stop_id}: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(arrival_time))}")

if __name__ == "__main__":
    parse_gtfs_rt()
