def fruit_weights(table: dict) -> dict:
    hash = {}

    for name, val in table.items():
        name = name.lower()

        if name not in hash:
            hash[name] = []

        hash[name].append(val)
    
    for fruit, val in hash.items():
        hash[fruit] = sum(val) // len(val)

    return hash