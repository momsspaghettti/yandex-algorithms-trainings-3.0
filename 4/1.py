from typing import List


def find_the_cheapest_path(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])

    dp = [[20 * 20 * 100 + 1 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = grid[i - 1][j - 1]
                continue

            dp[i][j] = min(
                dp[i - 1][j],
                dp[i][j - 1],
            ) + grid[i - 1][j - 1]

    return dp[n][m]


if __name__ == '__main__':
    n_, m_ = map(int, input().split(' '))
    print(find_the_cheapest_path(
        [
            list(map(int, input().split(' ')[:m_])) for _ in range(n_)
        ]
    ))
