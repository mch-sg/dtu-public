def count_differences(filename1: str, filename2: str) -> int:
    with open(filename1) as f: content1 = f.read().split(',')
    with open(filename2) as f: content2 = f.read().split(',')
    res = 0

    if len(content1) != len(content2):
        return -1
    
    for r1, r2 in zip(content1, content2):
        r1, r2 = int(r1.strip()), int(r2.strip())
        if r1 != r2: res += 1
    
    return res