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
    shutdown = get_shutdown_events(logfile)
    
    if len(shutdown) < 2:
        return timedelta()
    
    timestamps_list = []
    for entry in shutdown:
        split_entry = entry.split()
        timestamp = split_entry[1]
        timestamps_list.append(logstamp_to_datetime(timestamp))
    
    timestamps.sort() 

    first_shutdown_time = timestamps_list[0]
    last_shutdown_time = timestamps_list[-1]

    time_difference = last_shutdown_time - first_shutdown_time
    return time_difference


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
