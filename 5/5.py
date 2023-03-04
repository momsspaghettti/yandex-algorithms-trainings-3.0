from typing import List, TextIO, Optional, Tuple


class Graph(List[List[int]]):
    pass


def read_graph(vertexes_count: int, r: TextIO) -> Graph:
    graph = Graph([[] for _ in range(vertexes_count)])
    for f in range(vertexes_count):
        t = 0
        for is_connected in map(int, r.readline().split(' ')[:vertexes_count]):
            if is_connected == 1:
                graph[f].append(t)
            t += 1
    return graph


def get_cycle(graph: Graph, colors: List[int], vertex: int, prev: int) -> Optional[Tuple[bool, List[int]]]:
    colors[vertex] = 1
    for neighbor in graph[vertex]:
        if colors[neighbor] == 1 and neighbor != prev:
            return False, [neighbor]
        if colors[neighbor] == 0:
            cycle_res = get_cycle(graph, colors, neighbor, vertex)
            if cycle_res is not None:
                end, cycle = cycle_res
                if end:
                    return True, cycle
                if neighbor not in cycle:
                    cycle.append(neighbor)
                    return False, cycle
                return True, cycle
    colors[vertex] = 2
    return None


def get_graph_cycle(graph: Graph, vertexes_count: int) -> Optional[List[int]]:
    colors = [0 for _ in range(vertexes_count)]
    for i in range(vertexes_count):
        if colors[i] == 0:
            cycle_res = get_cycle(graph, colors, i, -1)
            if cycle_res is not None:
                return cycle_res[1]
    return None


def solve():
    with open('input.txt', 'r') as r:
        n = int(r.readline())
        g = read_graph(n, r)

    cycle = get_graph_cycle(g, n)
    if cycle is None:
        print('NO')
    else:
        print('YES')
        print(len(cycle))
        print(' '.join(map(lambda i: str(i + 1), cycle)))


if __name__ == '__main__':
    solve()
