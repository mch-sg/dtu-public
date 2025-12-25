def number_statistics(filename: str, number: int) -> list:
    with open(filename) as f: data = f.read().strip().splitlines()
    arr = []
    data = list(filter(None, data))

    for i in range(len(data)):
        nums = data[i].split(' ')
        arr.append(nums.count(f'{number}'))
    
    return arr