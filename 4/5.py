from typing import List


def get_longest_common_subsequence(first: List[int], second: List[int]) -> List[int]:
    n = len(first)
    m = len(second)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                continue
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i][j - 1]
            )

    res = []
    i = n
    j = m
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            res.append(first[i - 1])
            i -= 1
            j -= 1

    return res[::-1]


if __name__ == '__main__':
    n_ = int(input())
    f = list(map(int, input().split(' ')[:n_]))
    m_ = int(input())
    s = list(map(int, input().split(' ')[:m_]))

    print(
        ' '.join(map(str, get_longest_common_subsequence(f, s)))
    )
