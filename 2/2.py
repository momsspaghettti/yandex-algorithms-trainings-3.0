from collections import deque
from typing import List


def process_card_playing(first_player_cards: List[int], second_player_cards: List[int]) -> str:
    first = deque()
    for f in first_player_cards:
        first.append(f)
    second = deque()
    for s in second_player_cards:
        second.append(s)

    max_turn_number = 10 ** 6
    turn_number = 1
    while turn_number <= max_turn_number:
        f_card = first.popleft()
        s_card = second.popleft()

        if f_card == 0 and s_card == 9 or f_card > s_card and (f_card != 9 or s_card != 0):
            first.append(f_card)
            first.append(s_card)
        elif s_card == 0 and f_card == 9 or s_card > f_card and (s_card != 9 or f_card != 0):
            second.append(f_card)
            second.append(s_card)
        else:
            return 'botva'

        if len(first) == 0:
            return f'second {turn_number}'

        if len(second) == 0:
            return f'first {turn_number}'

        turn_number += 1

    return 'botva'


if __name__ == '__main__':
    print(process_card_playing(
        list(map(int, input().split())),
        list(map(int, input().split()))))
