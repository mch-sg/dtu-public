def arrival_times(schedule: list[str], delay: int) -> list[str]:
    arr = []
    for time in schedule:
        hour, minute = time.split(':')
        minute = int(minute) + delay
        hour = int(hour) + minute // 60
        hour %= 24
        minute %= 60
        arr.append(f'{hour:02}:{minute:02}')
    return arr