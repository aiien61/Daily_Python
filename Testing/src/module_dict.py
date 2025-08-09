from typing import Any

def update_value_by_key(origin_dict: dict, key: str, value: Any) -> dict:
    if key not in origin_dict:
        raise KeyError
    
    new_dict = origin_dict
    new_dict[key] = value
    return new_dict

def check_key_exists(my_dict: dict, key: str) -> bool:
    return True if key in my_dict else False
