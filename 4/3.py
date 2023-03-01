def get_max_knight_move_ways(n: int, m: int) -> int:
    dp = [[0 for _ in range(m)] for _ in range(n)]

    possible_moves = [(-2, -1), (-1, -2)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            for move in possible_moves:
                prev_i = i + move[0]
                prev_j = j + move[1]
                if prev_i < 0 or prev_j < 0:
                    continue
                dp[i][j] += dp[prev_i][prev_j]

    return dp[n - 1][m - 1]


if __name__ == '__main__':
    n_, m_ = map(int, input().split(' '))
    print(get_max_knight_move_ways(n_, m_))
