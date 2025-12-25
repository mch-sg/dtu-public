def graph_transpose(graph: dict) -> dict:
    transposed = {}
    for node, edges in graph.items():
        for k in range(len(edges)):
            if edges[k] not in transposed:
                transposed[edges[k]] = []

            transposed[edges[k]].append(node)
    
    return transposed