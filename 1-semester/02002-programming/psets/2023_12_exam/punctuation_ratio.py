def punctuation_ratio(text: str) -> float:
    with_c = int(text.count(', and '))
    without_c = int(text.count('and ')) - with_c

    if with_c == 0 or without_c == 0: 
        return 0
    
    ratio = with_c / without_c

    return ratio