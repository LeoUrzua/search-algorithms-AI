from SearchByDepth import find_by_deep
from SearchByBreadth import find_breadth_path

def swap(difference, parent):
    tb = list(parent)
    x, y = tb.index(white_space), tb.index(white_space) + difference
    tb[x], tb[y] = tb[y], tb[x]
    tb = ''.join(tb)
    set_game(tb, parent)


def position(d, p):
    for i in d:
        swap(i, p)


def f(x, p):
    right = 1
    left = -1
    down = 3
    up = -3
    if x == 0:
        # left_upper_corner(p)
        position([right, down], p)
    elif x == 1:
        # upper_middle(p)
        position([right, left, down], p)
    elif x == 2:
        position([right, left], p)
    elif x == 3:
        position([up, right, down], p)
    elif x == 4:
        position([right, left, down, up], p)
    elif x == 5:
        position([up, left, down], p)
    elif x == 6:
        position([right, up], p)
    elif x == 7:
        position([right, left, up], p)
    elif x == 8:
        position([up, left], p)
    else:
        print("Internal error system")


def set_game(table, parent):
    if table not in game:
        game[parent].append(table)
        game[table] = []

    if table not in parents:
        parents.append(table)
    return None


def print_game():
    for item in game.items():
        print(item)
    print("--------------")


def generate_game():
    n_possible_state = 181440
    for i in range(n_possible_state):
        f(parents[i].index(white_space), parents[i])
        if parents[i] == last:
            return True
    return False


if __name__ == '__main__':
    white_space = "*"
    first = "2831647*5"
    table = first
    parents = [table]
    last = "123*84765"
    game = {table: []}
    if generate_game():
        depth_route = find_by_deep(game, first, last)
        breadth_route = find_breadth_path(game, first, last)
        print("shortest path by depth: ", depth_route)
        print("shortest path by breadth: ", depth_route)


    else:
        print("This target can't exist")



