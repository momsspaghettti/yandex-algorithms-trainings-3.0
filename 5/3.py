from typing import List, Set, TextIO


class Graph(List[Set[int]]):
    pass


def can_mark_with_two_colors(graph: Graph, colors: List[int], vertex: int) -> bool:
    stack = [(vertex, 1)]
    while len(stack) > 0:
        v, color = stack.pop()
        colors[v] = color
        for neighbor in graph[v]:
            if colors[neighbor] == color:
                return False
            if colors[neighbor] == 0:
                stack.append((neighbor, 3 - color))
    return True


def read_graph(vertexes_count: int, edges_count: int, r: TextIO) -> Graph:
    graph = Graph([set() for _ in range(vertexes_count)])
    for _ in range(edges_count):
        f, t = map(int, r.readline().split(' ')[:2])
        if f == t:
            continue
        f -= 1
        t -= 1
        graph[f].add(t)
        graph[t].add(f)
    return graph


def can_mark_graph_with_two_colors(graph: Graph, vertexes_count: int) -> bool:
    colors = [0 for _ in range(vertexes_count)]
    for i in range(vertexes_count):
        if colors[i] == 0:
            if not can_mark_with_two_colors(graph, colors, i):
                return False
    return True


def solve():
    with open('input.txt', 'r') as r:
        n, m = map(int, r.readline().split(' ')[:2])
        g = read_graph(n, m, r)

    if can_mark_graph_with_two_colors(g, n):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    solve()
