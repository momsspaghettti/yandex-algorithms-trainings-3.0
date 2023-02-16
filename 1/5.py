from typing import List


def get_relocation_solution(cities_life_costs: List[int]) -> List[int]:
    stack = []
    res = [-1 for _ in range(len(cities_life_costs))]

    for i in range(len(cities_life_costs)):
        cost = cities_life_costs[i]
        while len(stack) > 0 and stack[-1][0] > cost:
            res[stack[-1][1]] = i
            stack.pop()
        stack.append((cost, i))

    return res


if __name__ == '__main__':
    input()
    print(' '.join(map(str, get_relocation_solution(list(map(int, input().split(' ')))))))
