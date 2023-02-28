def solve(n: int, k: int) -> int:
    dp = [0 for _ in range(k)]
    dp[0] = 1
    if k > 1:
        dp[1] = 1
    for i in range(2, k):
        for j in range(i):
            dp[i] += dp[j]

    if n <= k:
        return dp[n - 1]

    for i in range(k, n):
        dp.append(0)
        for j in range(k):
            dp[i] += dp[i - 1 - j]

    return dp[n - 1]


if __name__ == '__main__':
    n_, k_ = map(int, input().split(' '))
    print(solve(n_, k_))
