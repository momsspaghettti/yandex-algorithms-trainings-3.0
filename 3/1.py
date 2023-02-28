def solve(n: int) -> int:
    if n <= 0:
        return 0

    dp = [0 for _ in range(max(3, n))]
    dp[0] = 2
    dp[1] = 4
    dp[2] = 7

    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n - 1]


if __name__ == '__main__':
    n_ = int(input())
    print(solve(n_))
