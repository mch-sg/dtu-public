def name_frequency(names: list[str]) -> dict:
    hash = {}
    for i, val in enumerate(names):
        # clean the data
        cleaned = val.split(' ')
        name = cleaned[0].title()

        # put the data in the bucket
        if name not in hash:
            hash[name] = 0

        hash[name] += 1

    return hash