def running_speed(pace: float) -> tuple:
    pace = 1 / pace
    kmh = pace * 60
    ms = pace * ((1000)/(60))
    return kmh, ms