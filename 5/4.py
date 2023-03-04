from typing import List, TextIO, Optional
import sys

sys.setrecursionlimit(100000)


class Graph(List[List[int]]):
    pass


def read_graph(vertexes_count: int, edges_count: int, r: TextIO) -> Graph:
    graph = Graph([[] for _ in range(vertexes_count)])
    for _ in range(edges_count):
        f, t = map(int, r.readline().split(' ')[:2])
        f -= 1
        t -= 1
        graph[f].append(t)
    return graph


def do_topologically_sorting(graph: Graph, colors: List[int], vertex: int, result: List[int]) -> bool:
    colors[vertex] = 1
    for neighbor in graph[vertex]:
        if colors[neighbor] == 1:
            return False
        if colors[neighbor] == 0:
            if not do_topologically_sorting(graph, colors, neighbor, result):
                return False
    colors[vertex] = 2
    result.append(vertex)
    return True


def get_graph_topologically_sorting(graph: Graph, vertexes_count: int) -> Optional[List[int]]:
    colors = [0 for _ in range(vertexes_count)]
    result = []
    for i in range(vertexes_count):
        if colors[i] == 0:
            if not do_topologically_sorting(graph, colors, i, result):
                return None
    return result[::-1]


def solve():
    with open('input.txt', 'r') as r:
        n, m = map(int, r.readline().split(' ')[:2])
        g = read_graph(n, m, r)

    topologically_sorting = get_graph_topologically_sorting(g, n)
    if topologically_sorting is None:
        print(-1)
    else:
        print(' '.join(map(lambda v: str(v + 1), topologically_sorting)))


if __name__ == '__main__':
    solve()
