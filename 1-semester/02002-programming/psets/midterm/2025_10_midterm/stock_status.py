def stock_status(number_of_items, days_to_delivery):
    if number_of_items >= 6:
        return f'In stock'
    elif number_of_items >= 1:
        return f'Only {number_of_items} left in stock'
    elif number_of_items == 0 and days_to_delivery > 0:
        return f'Available in {days_to_delivery} days'
    elif number_of_items == 0 and days_to_delivery == 0:
        return f'Out of stock'
    else:
        return 'Unknown'