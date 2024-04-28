from urllib.request import urlopen
from datetime import datetime

time_difference = 0
last_update = 0

def get_current_time_online():
    res = urlopen('http://just-the-time.appspot.com/')
    datetime_string = res.read().strip()
    return datetime.strptime(datetime_string.decode(), '%Y-%m-%d %H:%M:%S')

def get_current_time_tunisia() -> datetime:
    return datetime.now() + time_difference


if ( time_difference == 0):
    try:
        current_datetime = datetime.now()
        time_difference = get_current_time_online() - current_datetime
        print("[utils] Time difference updated successfully. Current time:", get_current_time_tunisia())
    except Exception :
        print("[utils] Error: Failed to update time from online source. Check your internet connection or try again later.")
