def sentence_complexities(filename: str) -> list:
    with open(filename) as f: sentences = f.read().strip()
    s = ''
    arr = []
    for char in sentences:
        if char.isalnum() or char == ' ' or char == '\n':
            s += char
    s = list(filter(None, s.split('\n')))

    for line in s:
        longest = 0
        chars = line.split(' ')
        amt_words = int(len(chars))

        for word in chars:
            if int(len(word)) > int(longest):
                longest = len(word)

        m = amt_words + longest
        arr.append(m)

    return arr