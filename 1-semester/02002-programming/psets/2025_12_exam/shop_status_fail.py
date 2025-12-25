def shop_status(day: str, hour: int) -> tuple:
    is_open = False
    day_change = ''
    hour_change = 0
    #days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days = {'Monday': list(range(9,17)),
            'Tuesday': list(range(9,17)),
            'Wednesday': list(range(9, 17)),
            'Thursday': list(range(9, 17)),
            'Friday': list(range(9, 17)),
            'Saturday': 0,
            'Sunday': 0}
    
    print(days)

    hour_today = days[day]

    print(day, hour_today)

    if day == 'Saturday' or day == 'Sunday':
        is_open = False
        day_change = 'Monday'
        hour_change = 9

    if day in days and hour in days[day]:
        is_open = True
        day_change = day
        hour_change = 17

    if hour not in days[day]:
        is_open = False
        day_change = 

    #for i, hrs in enumerate(hour_today):
    #    if hour == hrs:
    #        index = i


    
    print("ii",hour, hour_today[-1], hour - hour_today[-1])

    #for day, hrs in days.items():
    #    print(day, hrs)

    return is_open, day_change, hour_change


print(shop_status('Monday', 17))