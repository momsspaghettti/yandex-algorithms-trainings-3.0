from typing import List


def get_unique_card_count_less_than_given_threshold(sorted_cards: List[int], threshold: int) -> int:
    if threshold > sorted_cards[-1]:
        return len(sorted_cards)
    if threshold <= sorted_cards[0]:
        return 0

    l = 0
    r = len(sorted_cards)
    mid = (l + r) // 2
    while l < r:
        mid = (l + r) // 2
        if sorted_cards[mid] == threshold:
            break
        if sorted_cards[mid] > threshold > sorted_cards[mid - 1]:
            break
        if sorted_cards[mid] < threshold:
            l = mid + 1
        else:
            r = mid
    return mid


if __name__ == '__main__':
    input()
    cards = sorted(
            set(
                map(
                    int,
                    input().split()
                )
            )
        )

    input()
    cache = {}
    for p in map(int, input().split()):
        if p in cache:
            print(cache[p])
        else:
            res = get_unique_card_count_less_than_given_threshold(cards, p)
            cache[p] = res
            print(res)
