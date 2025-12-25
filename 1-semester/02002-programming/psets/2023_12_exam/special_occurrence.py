def special_occurrence(sequence: list[int]) -> int:
    seq, idx = sequence, 0
    for current, n1, n2 in zip(seq, seq[1:], seq[2:]):
        if (current == 5) and ((n1 == 7 and n2 != 7) or (n1 != 7 and n2 == 7)):
            return idx
        idx += 1
    return -1