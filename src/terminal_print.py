import time
from config import STOP_ID_DIRECTION

def print_to_terminal(time_table):

    print(f"\n--- {time.strftime('%H:%M - %m/%d/%Y')} ---")
    for route, directions in time_table.items():
        for direction, trains in directions.items():
            print(f"{route} to {STOP_ID_DIRECTION[direction]} in {trains}")

