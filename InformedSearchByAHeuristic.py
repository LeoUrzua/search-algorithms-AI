def find_by_heuristic_a(graph, start, end, l = []):
    if start == end:
        print("Found")
        return
    l.extend(graph[start])
    value = []
    for element in l:
        similar = similarity(element, end)
        value.append(similar)
    print(l, "--- current nodes")
    print(value, "--- heuristic values")
    best_option = l[value.index(max(value))]
    print(best_option, "--- best option")
    l.remove(best_option)
    print(l, "non-visited nodes")
    print("----------------------")
    find_by_heuristic_a(graph, best_option, end)


def similarity(current, end):
    sim = 0
    for i in current:
        if current.index(i) == end.index(i):
            sim = sim +1
    return sim
