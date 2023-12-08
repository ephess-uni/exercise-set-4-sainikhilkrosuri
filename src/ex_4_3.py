""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    shutdown_entries = get_shutdown_events(logfile)
    if len(shutdown_entries) < 2:
        return timedelta()  # No sufficient entries to calculate time difference
    
    timestamps = [entry.split()[1] for entry in shutdown_entries]  # Extract timestamps
    timestamps.sort()  # Sort timestamps to get the first and last shutdown times

    first_shutdown_time = logstamp_to_datetime(timestamps[0])
    last_shutdown_time = logstamp_to_datetime(timestamps[-1])

    return last_shutdown_time - first_shutdown_time


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
