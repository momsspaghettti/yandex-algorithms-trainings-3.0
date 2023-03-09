from typing import List, TextIO, Optional, Tuple
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


def compute_distance_and_path(graph: Graph, from_: int, to_: int) -> Tuple[int, List[int]]:
    if to_ == from_:
        return 0, []

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

    if graph[to_].distance is None:
        return -1, []

    path = [to_]
    curr = to_
    while curr != from_:
        for neighbor in graph[curr].neighbors:
            if graph[neighbor].distance is None:
                continue
            if graph[neighbor].distance + 1 == graph[curr].distance:
                curr = neighbor
                break
        path.append(curr)

    return graph[to_].distance, path[::-1]


def solve():
    with open('input.txt', 'r') as r:
        n = int(r.readline())
        g = read_graph(n, r)
        f, t = map(int, r.readline().split(' ')[:2])

    distance, path = compute_distance_and_path(g, f - 1, t - 1)
    print(distance)
    if len(path) > 0:
        print(' '.join(map(lambda v: str(v + 1), path)))


if __name__ == '__main__':
    solve()
