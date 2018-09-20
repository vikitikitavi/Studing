graph = {
    1: [(2, 5), (3,0)],
    2: [(4, 15), (5, 20)],
    3: [(4, 30), (5, 35)],
    4: [(6, 20)],
    5: [(6, 10)],
    6: [],
}

def process_score_table(graph, scores):
    not_processed = set([node for node, connection in scores.items() if connection])

    while not_processed:
        min_node, score = min([(node, scores.get(node)[1]) for node in not_processed], key=lambda x: x[1])
        not_processed.remove(min_node)
        for conecting_node, weight in graph.get(min_node):
            connection_weight =  score + weight
            if not scores[conecting_node] or scores[conecting_node][1] > connection_weight:
                scores[conecting_node]  = (min_node, connection_weight)
                not_processed.add(conecting_node)

def get_finish_node(graph):
    for node in graph.keys():
        if not graph[node]:
            return node

def get_path(finish_node, scores):
    connecting_node = scores.get(finish_node)
    path = [finish_node]
    while connecting_node:
        path.append(connecting_node[0])
        connecting_node = scores.get(connecting_node[0])
    return path[::-1]

def init_score_table(graph, start_node=1):
    result = dict(map(lambda x: (x, None), graph.keys()))
    for start_connection in graph.get(start_node, {}):
        result[start_connection[0]] = (start_node, start_connection[1])
    return result


scores = init_score_table(graph)
process_score_table(graph, scores)

finish_node = get_finish_node(graph)
path = get_path(finish_node, scores)
score = scores.get(finish_node)[1]

print(f"Optimal path: {path}")
print(f"Score: {score}")