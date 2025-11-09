def punctuation_ratio(text):
    str = ' and '
    str2 = ', and '
    no_comma = 0
    with_comma = 0

    if str in text: # If no comma is in text
        no_comma = text.count(str)

    if str2 in text: # If with comma is in text
        with_comma = text.count(str2)
    
    no_comma -= with_comma # There will be double of no comma because of with comma, so i remove those here.
    ratio = 0.0
    if no_comma == 0 or with_comma == 0:
        ratio = 0
    else:
        ratio = (with_comma)/(no_comma)

    return ratio