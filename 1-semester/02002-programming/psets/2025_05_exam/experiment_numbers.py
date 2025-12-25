def experiment_numbers(experiments: list[str]) -> dict:
    hash = {}
    for i in experiments:
        name, repetition = i.split('-')
        if name not in hash: 
            hash[name] = int(repetition)

        if int(repetition) > hash[name]: 
            hash[name] = int(repetition)

    return hash