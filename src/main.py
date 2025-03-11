from config import FEED_URLS
from api import parse_gtfs_rt
import time
from terminal_print import print_to_terminal

def main():
    """Continuously print GTFS-RT arrivals every minute."""
    while True:
        time_table = {}
        for route_id, feed_url in FEED_URLS.items():
            time_table[route_id] = parse_gtfs_rt(feed_url)

        print_to_terminal(time_table)
        time.sleep(60)  # Wait 60 seconds before refreshing

    print(time_table)

if __name__ == "__main__":
    main()