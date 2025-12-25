def navigation_tracking(instructions: list[int]) -> list:
    i = 0
    prev = 0
    ins = instructions
    pos = ins[0]
    visited = [ins[0]]

    while len(ins) > 0:
        if len(instructions) > 0:
            i = (prev + pos) % len(instructions)
        pos = ins[i]
        prev = i
        visited.append(pos)

        if visited.count(pos) > ins.count(pos):
            visited.pop()
            break

    return visited

print(navigation_tracking([2, 5, 1, 3, 4, 2, 1, 1, 6, 2])) 