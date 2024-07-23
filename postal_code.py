#!/usr/bin/python3
import re as regex

def is_valid_code(zip_code: str) -> bool:
    """Check if zip code is valid return true
    Args:
        zip_code (str): _description_
    Returns:
        bool: _description_
    """
    pattern = regex.compile(r'^([\d]{5})-[\d]{5}$')
    matched = pattern.search(zip_code)
    if matched:
        print(matched.group(1))
    return bool(matched)    

zip_codes = [
    '12345-12345',
    '12345-hello',
    '12345-123',
    '1234-12345',
    '123456',
    '123.4-56789',
]

print(*filter(is_valid_code, zip_codes), sep='\n')