from typing import List, Tuple


def get_min_queue_time(n: int, q: List[Tuple[int, ...]]) -> int:
    if n <= 0:
        return 0

    dp = [0 for _ in range(n)]
    dp[0] = q[0][0]

    def get_dp(ind: int) -> int:
        if ind >= 0:
            return dp[ind]
        return 0

    def get_q(ind: int, inner_ind: int) -> int:
        if ind >= 0:
            return q[ind][inner_ind]
        return 3601

    for i in range(1, n):
        dp[i] = min(
            get_dp(i - 1) + get_q(i, 0),
            get_dp(i - 2) + get_q(i - 1, 1),
            get_dp(i - 3) + get_q(i - 2, 2)
        )

    return dp[n - 1]


if __name__ == '__main__':
    n_ = int(input())
    print(get_min_queue_time(
        n_,
        [tuple(map(int, filter(lambda s: len(s) > 0, input().split(' ')))) for _ in range(n_)]))
