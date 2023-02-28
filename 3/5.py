from typing import List


def get_min_length(arr: List[int]) -> int:
    arr = list(sorted(set(arr)))
    n = len(arr)

    dp = [0 for _ in range(n)]
    dp[1] = arr[1] - arr[0]

    for i in range(2, n):
        if i + 1 == n:
            dp[i] = dp[i - 1] + arr[i] - arr[i - 1]
            continue

        dp[i] = min(
            dp[i - 1] + arr[i] - arr[i - 1],
            dp[i - 2] + arr[i - 1] - arr[i - 2]
        )

    return dp[n - 1]


if __name__ == '__main__':
    input()
    print(get_min_length(
        list(map(int, filter(lambda s: len(s) > 0, input().split(' '))))
    ))
