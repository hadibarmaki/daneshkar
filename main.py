#!/usr/bin/python3
class DiscountError(Exception):
    pass


def apply_discount(price: int, discount: float = 0.0) -> int:
    """Calculates the Final Price After Discount 
    """
    final_price = int(price * (1 - discount))
    if not 0 <= final_price < price:
        raise DiscountError('Invalid price')
    
    return final_price
