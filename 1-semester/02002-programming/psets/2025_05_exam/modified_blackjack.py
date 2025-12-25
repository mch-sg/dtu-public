def modified_blackjack(cards: list[int]) -> tuple:
    for n in range(len(cards)):
        res = 0
        k_idx = 0
        for k in range(n, len(cards)):
            res += cards[k]
            k_idx += 1

            if res == 21: 
                return (n, k_idx)
            if res > 21: break

    return (-1, -1)