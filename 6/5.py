from typing import List, TextIO, Optional, Set
from collections import deque


class Vertex:
    def __init__(self):
        self.distance: Optional[int] = None
        self.neighbors: Set[int] = set()


class Graph(List[Vertex]):
    pass


def read_graph(vertexes_count: int, r: TextIO) -> Graph:
    graph = Graph([Vertex() for _ in range(vertexes_count)])
    lines_count = int(r.readline())
    for _ in range(lines_count):
        line = r.readline().split(' ')
        line_len = int(line[0])
        line_int = list(map(int, line[1:line_len + 1]))
        for i in range(line_len):
            for j in range(i + 1, line_len):
                f = line_int[i] - 1
                s = line_int[j] - 1
                graph[f].neighbors.add(s)
                graph[s].neighbors.add(f)
    return graph


def compute_distance(graph: Graph, from_: int, to_: int) -> int:
    if to_ == from_:
        return 0

    queue = deque()
    queue.append((from_, 0))
    while len(queue) > 0:
        v, d = queue.popleft()
        if graph[v].distance is None:
            graph[v].distance = d
        else:
            graph[v].distance = min(graph[v].distance, d)
        for neighbor in filter(lambda n: graph[n].distance is None, graph[v].neighbors):
            queue.append((neighbor, d + 1))

    return -1 if graph[to_].distance is None else graph[to_].distance - 1


def solve():
    with open('input.txt', 'r') as r:
        n = int(r.readline())
        g = read_graph(n, r)
        f, t = map(int, r.readline().split(' ')[:2])

    distance = compute_distance(g, f - 1, t - 1)
    print(distance)


if __name__ == '__main__':
    solve()
