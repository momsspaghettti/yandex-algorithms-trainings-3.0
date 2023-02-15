def get_closest_seat_number(variants_count: int, is_right_seat: bool) -> int:
    if variants_count % 2 == 0:
        if is_right_seat:
            return 1
        else:
            return 2
    if is_right_seat:
        return 2
    return 1


def get_same_variant_answer(
        students_count: int,
        variants_count: int,
        row_number: int,
        is_right_seat: bool) -> str:
    if variants_count == students_count:
        return '-1'
    max_rows_count = students_count // 2 + students_count % 2

    closest_row_number_behind = row_number + variants_count // 2
    if variants_count % 2 != 0 and not is_right_seat:
        closest_row_number_behind += 1

    closest_row_number_ahead = row_number - variants_count // 2
    if variants_count % 2 != 0 and is_right_seat:
        closest_row_number_ahead -= 1

    closest_seat_number = get_closest_seat_number(variants_count, is_right_seat)

    if closest_row_number_behind < max_rows_count or \
            (closest_row_number_behind == max_rows_count and
             (students_count % 2 == 0 or closest_seat_number == 1)):
        if closest_row_number_ahead >= 1:
            if closest_row_number_behind - row_number <= row_number - closest_row_number_ahead:
                return f'{closest_row_number_behind} {closest_seat_number}'
            return f'{closest_row_number_ahead} {closest_seat_number}'
        return f'{closest_row_number_behind} {closest_seat_number}'

    if closest_row_number_ahead >= 1:
        return f'{closest_row_number_ahead} {closest_seat_number}'
    return '-1'


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    rn = int(input())
    rl_seat = int(input())

    print(get_same_variant_answer(n, k, rn, rl_seat == 1))
