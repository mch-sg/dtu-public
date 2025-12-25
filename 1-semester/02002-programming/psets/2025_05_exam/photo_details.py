def photo_details(filename: str) -> dict:
    date, number = filename.split('_')
    year, month, day = date[:4], date[4:6], date[6:]
    number, ext = number.split('.')
    return {
        'year': year,
        'month': month,
        'day': day,
        'number': number,
        'ext': ext
    }