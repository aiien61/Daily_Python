from module_external import call_external_api

def square(num: int) -> int:
    return num ** 2

def check_response_greater_than_0_5():
    external_result = call_external_api()
    response_value = external_result.get("response_value", None)
    if response_value is None:
        raise KeyError("response_value not exists.")
    
    return False if response_value <= 0.5 else True
