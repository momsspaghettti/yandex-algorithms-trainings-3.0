from typing import List, Set, TextIO


class Graph(List[Set[int]]):
    pass


def dfs(graph: Graph, visited: List[int], vertex: int, marker: int):
    stack = [vertex]
    while len(stack) > 0:
        v = stack.pop()
        visited[v] = marker
        for neighbor in graph[v]:
            if visited[neighbor] == 0:
                stack.append(neighbor)


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


def get_connectivity_components(graph: Graph, vertexes_count: int) -> List[List[int]]:
    visited = [0 for _ in range(vertexes_count)]
    marker = 1
    for i in range(vertexes_count):
        if visited[i] == 0:
            dfs(graph, visited, i, marker)
            marker += 1

    if marker == 1:
        return []
    result = [[] for _ in range(marker - 1)]
    for i in range(vertexes_count):
        result[visited[i] - 1].append(i + 1)
    return result


def solve():
    with open('input.txt', 'r') as r:
        n, m = map(int, r.readline().split(' ')[:2])
        g = read_graph(n, m, r)

    connectivity_components = get_connectivity_components(g, n)
    print(len(connectivity_components))
    for component in connectivity_components:
        print(len(component))
        print(' '.join(map(str, component)))


if __name__ == '__main__':
    solve()
