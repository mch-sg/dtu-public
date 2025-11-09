def compound_interest(principal, rate, frequency):
    rr = principal * (1 + (rate)/(frequency))**frequency - principal
    return rr