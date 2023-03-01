from typing import List, Tuple


def find_path_with_max_cost(grid: List[List[int]]) -> Tuple[int, List[str]]:
    n = len(grid)
    m = len(grid[0])

    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = grid[i - 1][j - 1]
                continue

            dp[i][j] = max(
                dp[i - 1][j],
                dp[i][j - 1],
            ) + grid[i - 1][j - 1]

    res_path = []
    i = n
    j = m
    while i != 1 or j != 1:
        if dp[i][j] - grid[i - 1][j - 1] == dp[i - 1][j]:
            res_path.append('D')
            i -= 1
        else:
            res_path.append('R')
            j -= 1

    return dp[n][m], res_path[::-1]


if __name__ == '__main__':
    n_, m_ = map(int, input().split(' '))

    max_cost, path = find_path_with_max_cost(
        [
            list(map(int, input().split(' ')[:m_])) for _ in range(n_)
        ]
    )

    print(max_cost)
    print(' '.join(path))
