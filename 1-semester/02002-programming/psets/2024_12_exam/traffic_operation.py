def traffic_operation(hour: int) -> str:
    hour = hour % 24
    if (hour >= 7 and hour < 9) or (hour >= 15 and hour < 17): return 'rush hour'
    if (hour >= 22 and hour < 24) or hour < 6: return 'night'
    else: return 'normal'