
from datetime import date, datetime
import pytz
import time


def print_current_time():
    while True:
        UTC = pytz.utc
        india_time = pytz.timezone('Asia/Kolkata')

        print(f"date : {datetime.now(india_time).strftime('%d-%b-%Y')}\nTime:{datetime.now(india_time).strftime('%H:%M:%S')}")

        time.sleep(1)


if __name__ == "__main__":
    print_current_time()
