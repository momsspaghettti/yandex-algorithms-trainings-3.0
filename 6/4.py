from typing import List, TextIO, Optional, Tuple
from collections import deque


class Vertex:
    def __init__(self):
        self.distance: Optional[int] = None
        self.neighbors: List[int] = []


class Graph(List[Vertex]):
    pass


def read_graph_and_speleologist_index(n: int, r: TextIO) -> Tuple[Graph, int]:
    cave = [[] for _ in range(n)]
    for i in range(n):
        r.readline()
        for _ in range(n):
            cave[i].append(r.readline()[:n])

    verges = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    speleologist_ind = -1
    graph = Graph([Vertex() for _ in range(n ** 3)])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ind = i * n * n + j * n + k
                c = cave[i][j][k]
                if c == '#':
                    continue
                if c == 'S':
                    speleologist_ind = ind
                for d_i, d_j, d_k in verges:
                    new_i = i + d_i
                    new_j = j + d_j
                    new_k = k + d_k
                    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or new_k < 0 or new_k >= n:
                        continue
                    if cave[new_i][new_j][new_k] == '#':
                        continue
                    neighbor_ind = new_i * n * n + new_j * n + new_k
                    graph[ind].neighbors.append(neighbor_ind)

    return graph, speleologist_ind


def compute_speleologist_distance(
        graph: Graph,
        n: int,
        speleologist_ind: int) -> int:
    if speleologist_ind < n * n:
        return 0

    queue = deque()
    queue.append((speleologist_ind, 0))
    while len(queue) > 0:
        v, d = queue.popleft()
        if graph[v].distance is None or graph[v].distance > d:
            graph[v].distance = d
        else:
            continue
        for neighbor in filter(lambda n_: graph[n_].distance is None, graph[v].neighbors):
            queue.append((neighbor, d + 1))

    return min(
        filter(lambda v_: v_.distance is not None, graph[:n * n]),
        key=lambda v_: v_.distance
    ).distance


def solve():
    with open('input.txt', 'r') as r:
        n = int(r.readline())
        g, ind = read_graph_and_speleologist_index(n, r)

    distance = compute_speleologist_distance(g, n, ind)
    print(distance)


if __name__ == '__main__':
    solve()
