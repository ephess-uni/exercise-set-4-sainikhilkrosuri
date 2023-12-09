""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    datestr = '2023-12-08T10:30:00'
    formated_str = '%Y-%m-%dT%H:%M:%S'
    final_dt = datetime.strptime(datestr, format_str)
    return final_dt


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
