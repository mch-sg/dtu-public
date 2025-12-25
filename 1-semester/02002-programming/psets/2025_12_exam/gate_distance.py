import math
def gate_distance(gate1: str, gate2: str) -> str:
    terminals = ['A', 'B', 'C', 'D']
    time = 0
    term1, gate1 = gate1[0], gate1[1:]
    term2, gate2 = gate2[0], gate2[1:]
    term1_idx = terminals.index(term1)
    term2_idx = terminals.index(term2)
    diff = abs(term2_idx - term1_idx)

    if term1 == term2:
        time = (4 * diff) + (max(int(gate1), int(gate2)) - min(int(gate1), int(gate2))) * 0.8
    else:
        time = (4 * diff) + (int(gate1) + int(gate2)) * 0.8
    
    return f'Walking time {math.ceil(time)} min'
