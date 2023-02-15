from typing import List, Tuple


def remove_from_list_at(list_: list, ind: int):
    list_[ind], list_[-1] = list_[-1], list_[ind]
    list_.pop()


def remove_intersecting_sections(sections: List[Tuple[int, int]], start: int, end: int):
    for i in range(len(sections) - 1, -1, -1):
        section = sections[i]
        s_start = section[0]
        s_end = section[1]

        if not (start > s_end or end < s_start):
            remove_from_list_at(sections, i)


def process_operation_systems_task():
    input()
    n = int(input())

    sections = []
    for _ in range(n):
        start, end = map(int, input().split())
        remove_intersecting_sections(sections, start, end)
        sections.append((start, end))

    print(len(sections))


if __name__ == '__main__':
    process_operation_systems_task()
