from typing import List


def get_max_string_goodness(letter_counts: List[int]) -> int:
    n = len(letter_counts)
    if n < 2:
        return 0

    min_id = 0
    min_ = letter_counts[min_id]
    for i in range(1, n):
        if letter_counts[i] < min_:
            min_ = letter_counts[i]
            min_id = i

    return (n - 1) * min_ + \
        get_max_string_goodness([c - min_ for c in letter_counts[:min_id]]) + \
        get_max_string_goodness([c - min_ for c in letter_counts[min_id + 1:]])


if __name__ == '__main__':
    n = int(input())
    c_list = []
    for _ in range(n):
        c_list.append(int(input()))

    print(get_max_string_goodness(c_list))
