def new_price(price: float, discount: int) -> tuple:
    rabat = price - (price*(discount/100))
    return rabat, f'{rabat:.2f} DKK'