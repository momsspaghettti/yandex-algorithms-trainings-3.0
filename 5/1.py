from typing import List, Set


class Graph(List[Set[int]]):
    pass


def dfs(graph: Graph, visited: List[bool], vertex: int):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)


def read_graph(vertexes_count: int, edges_count: int) -> Graph:
    graph = Graph([set() for _ in range(vertexes_count)])
    for _ in range(edges_count):
        f, t = map(int, input().split(' ')[:2])
        if f == t:
            continue
        f -= 1
        t -= 1
        graph[f].add(t)
        graph[t].add(f)
    return graph


def solve(graph: Graph, vertexes_count: int) -> List[int]:
    visited = [False for _ in range(vertexes_count)]
    dfs(graph, visited, 0)
    result = []
    for i in range(vertexes_count):
        if visited[i]:
            result.append(i + 1)
    return result


if __name__ == '__main__':
    n, m = map(int, input().split(' ')[:2])
    g = read_graph(n, m)
    res = solve(g, n)
    print(len(res))
    print(' '.join(map(str, res)))
