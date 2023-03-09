from typing import TextIO
from collections import deque


def compute_all_fleas_distance(
        n: int,
        m: int,
        f_x: int,
        f_y: int,
        fleas_count: int,
        r: TextIO) -> int:
    if fleas_count == 0:
        return 0

    graph = [[-1 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((f_x, f_y, 0))

    turns = [
        (2, 1), (-2, -1), (1, 2), (-1, -2),
        (-2, 1), (2, -1), (-1, 2), (1, -2)
    ]

    while len(queue) > 0:
        x, y, d = queue.popleft()
        if graph[x][y] == -1 or graph[x][y] > d:
            graph[x][y] = d
        else:
            continue
        for dx, dy in turns:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            if graph[new_x][new_y] == -1:
                queue.append((new_x, new_y, d + 1))

    total_distance = 0
    for _ in range(fleas_count):
        flea_x, flea_y = map(int, r.readline().split(' ')[:2])
        flea_x -= 1
        flea_y -= 1
        if graph[flea_x][flea_y] == -1:
            return -1
        total_distance += graph[flea_x][flea_y]
    return total_distance


def solve():
    with open('input.txt', 'r') as r:
        n_, m_, s_, t_, q_ = map(int, r.readline().split(' ')[:5])
        distance = compute_all_fleas_distance(n_, m_, s_ - 1, t_ - 1, q_, r)
        print(distance)


if __name__ == '__main__':
    solve()
