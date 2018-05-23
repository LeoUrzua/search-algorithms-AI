from difflib import SequenceMatcher


def similarity(current, end):
    # return SequenceMatcher(None, current, end).ratio()
    sim = 0
    for i in current:
        # print(i)
        # res = current.index(i)-end.index(i)
        if current.index(i) == end.index(i):
            sim = sim +1
        # print(sim)
    # return SequenceMatcher(None, current, end).ratio()
    # print("---------------  ", sim )
    return sim + SequenceMatcher(None, current, end).ratio()


def similarity2(elements, end):
    val = 0
    for elem in elements:
        val += similarity(elem, end)
        if len(elements) == 0:
            return 0
    return val/len(elements)


def similarity3(elements, end):
    val = []
    for elem in elements:
        a = similarity(elem, end)
        val.extend([a])
    if len(val) == 0:
        return 0
    return max(val)


def find_double_heuristic_a(graph, start, end, l = []):
    if start == end:
        print("Found")
        return
    l.extend(graph[start])
    value = []
    for element in l:
        similar = similarity(element, end) + similarity3(graph[element], end)
        value.append(similar)
    print(l, "--- current nodes")
    print(value, "--- heuristic values")
    best_option = l[value.index(max(value))]
    print(best_option, "--- best option")
    l.remove(best_option)
    print(l, "non-visited nodes")
    print("----------------------")
    find_double_heuristic_a(graph, best_option, end)
