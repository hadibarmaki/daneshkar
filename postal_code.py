#!/usr/bin/python3
def is_valid_code(zip_code: str) -> bool:
    """Check if zip code is valid return true
    Args:
        zip_code (str): _description_
    Returns:
        bool: _description_
    """
    return (
        isinstance(zip_code, str)
        and len(zip_code) == 11
        and zip_code[5] == '-'
        and zip_code[:5].isdigit()
        and zip_code[6:].isdigit()
    )

zip_codes = [
    '12345-12345',
    '12345-hello',
    '12345-123',
    '1234-12345',
    '123456',
    '123.4-56789',
]

print(list(filter(is_valid_code, zip_codes)))