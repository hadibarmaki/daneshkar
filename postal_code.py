#!/usr/bin/python3
import re as regex

def is_valid_code(zip_code: str) -> bool:
    """Check if zip code is valid return true
    Args:
        zip_code (str): _description_
    Returns:
        bool: _description_
    """
    return bool(regex.search('[\d]{5}-[\d]{5}', zip_code))

zip_codes = [
    '12345-12345',
    '12345-hello',
    '12345-123',
    '1234-12345',
    '123456',
    '123.4-56789',
]

print(list(filter(is_valid_code, zip_codes)))