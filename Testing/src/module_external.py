import time
import random

def call_external_api() -> dict:
    time.sleep(0.5)
    if random.random() < 0.5:
        return {}
    
    response_value: float = random.random()
    return {"response_value": response_value}
