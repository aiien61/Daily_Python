import time
from datetime import datetime

def get_current_month() -> int:
    today: datetime = datetime.now()
    month: int = today.month
    if month < 0:
        raise Exception("Wrong month.")
    return today.month

def sleep_for_a_while(seconds: int) -> int:
    print("Ready for sleeping")
    time.sleep(seconds)
    return seconds
