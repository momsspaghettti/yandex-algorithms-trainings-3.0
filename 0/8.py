max_value = 1_000_000_000


def find_min_rectangle():
    k = int(input())

    left_bottom_x, left_bottom_y = max_value, max_value
    right_top_x, right_top_y = -max_value, -max_value

    for _ in range(k):
        x, y = map(int, input().split())
        left_bottom_x = min(left_bottom_x, x)
        left_bottom_y = min(left_bottom_y, y)

        right_top_x = max(right_top_x, x)
        right_top_y = max(right_top_y, y)

    print(left_bottom_x, left_bottom_y, right_top_x, right_top_y, end=' ')


if __name__ == '__main__':
    find_min_rectangle()
