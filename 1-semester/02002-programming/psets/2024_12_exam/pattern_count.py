def pattern_count(filename: str, pattern: str) -> int:
    with open(filename) as f: content = f.read().strip().splitlines()
    strs = ''
    res = 0
    for v in range(len(content)): strs = strs + content[v]
    for i, val in enumerate(strs):
        if strs[i:i + len(pattern)] == pattern:
            res += 1
    return res