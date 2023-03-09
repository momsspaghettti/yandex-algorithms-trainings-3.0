from typing import List, TextIO, Optional
from collections import deque


class Vertex:
    def __init__(self):
        self.distance: Optional[int] = None
        self.neighbors: List[int] = []


class Graph(List[Vertex]):
    pass


def read_graph(vertexes_count: int, r: TextIO) -> Graph:
    graph = Graph([Vertex() for _ in range(vertexes_count)])
    for f in range(vertexes_count):
        t = 0
        for is_connected in map(int, r.readline().split(' ')[:vertexes_count]):
            if is_connected == 1:
                graph[f].neighbors.append(t)
            t += 1
    return graph


def compute_distance(graph: Graph, from_: int, to_: int) -> int:
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

    return -1 if graph[to_].distance is None else graph[to_].distance


def solve():
    with open('input.txt', 'r') as r:
        n = int(r.readline())
        g = read_graph(n, r)
        f, t = map(int, r.readline().split(' ')[:2])

    distance = compute_distance(g, f - 1, t - 1)
    print(distance)


if __name__ == '__main__':
    solve()
