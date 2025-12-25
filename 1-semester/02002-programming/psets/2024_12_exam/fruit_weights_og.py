import math
def fruit_weights(table: dict) -> dict:
    d = {}
    keys = [i.lower() for i, v in table.items()]
    #print(keys, keys.count('orange'))
    res = 0

    for i, val in table.items():
        res = 0
        count = 1
        for k, v in table.items():
            if keys.count(i.lower()) == 1: res += val; d[i.lower()] = res; break
            if i == k.lower() or (i == k.title() and i.lower() not in d):
                if i == k: res += val; d[i.lower()] = res
                if val != v:
                    res += v
                    count += 1
                    d[i.lower()] = math.floor(res/count)
            #print(d)
    return d
    