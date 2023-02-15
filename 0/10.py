def solve(string: str):
    n = len(string)
    res = {}
    for i in range(n):
        if string[i] not in res:
            res[string[i]] = 0
        res[string[i]] += (i + 1) * (n - i)

    for l_ in sorted(res):
        print(f'{l_}: {res[l_]}')


if __name__ == '__main__':
    solve(input())
