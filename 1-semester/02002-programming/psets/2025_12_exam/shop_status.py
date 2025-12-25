def shop_status(day: str, hour: int) -> tuple:
    is_open = False
    day_change = ''
    hour_change = 0
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    if day == 'Saturday' or day == 'Sunday':
        is_open = False
        day_change = 'Monday'
        hour_change = 9

        return is_open, day_change, hour_change

    day_index = days.index(day)

    if day in days and (9 <= hour < 17):
        is_open = True
        day_change = day
        hour_change = 17

    if day in days and hour < 9:
        is_open = False
        day_change = day
        hour_change = 9

    if day == 'Friday' and hour >= 17:
        is_open = False
        day_change = 'Monday'
        hour_change = 9
    elif day in days and hour >= 17:
        is_open = False
        day_change = days[day_index + 1]
        hour_change = 9

    return is_open, day_change, hour_change