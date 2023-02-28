from typing import Tuple, List


def calculator(n: int) -> Tuple[int, List[int]]:
    if n == 1:
        return 0, [1]

    dp = [0 for _ in range(n + 1)]
    prev_arr = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        res = dp[i - 1]
        prev = i - 1
        if i % 2 == 0 and i // 2 > 0 and dp[i // 2] < res:
            res = dp[i // 2]
            prev = i // 2

        if i % 3 == 0 and i // 3 > 0 and dp[i // 3] < res:
            res = dp[i // 3]
            prev = i // 3

        dp[i] = res + 1
        prev_arr[i] = prev

    res = [n]
    i = n
    while prev_arr[i] != 0:
        res.append(prev_arr[i])
        i = prev_arr[i]

    return dp[n], res[::-1]


if __name__ == '__main__':
    n_ = int(input())
    count, nums = calculator(n_)
    print(count)
    print(' '.join(map(str, nums)))
