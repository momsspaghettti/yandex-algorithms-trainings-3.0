from typing import List


def is_wagons_problem_can_be_solved(wagons_numbers: List[int]) -> bool:
    needed_number = 1
    stack = []
    for num in wagons_numbers:
        stack.append(num)
        while len(stack) > 0 and stack[-1] == needed_number:
            stack.pop()
            needed_number += 1

    return len(stack) == 0


if __name__ == '__main__':
    input()
    if is_wagons_problem_can_be_solved(list(map(int, input().split(' ')))):
        print('YES')
    else:
        print('NO')
