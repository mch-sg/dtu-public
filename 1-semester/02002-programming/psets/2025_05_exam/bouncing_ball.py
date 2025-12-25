def bouncing_ball(h0: float) -> int:
    dt = 0
    while h0 >= 1:
        h0 = (2 / 3) * h0
        dt += 1

    return dt