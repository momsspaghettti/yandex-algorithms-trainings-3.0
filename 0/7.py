import math

day_seconds = 24 * 60 * 60


def get_seconds(hours: int, minutes: int, seconds: int) -> int:
    return 60 * 60 * hours + 60 * minutes + seconds


def make_number_two_digits(number: int) -> str:
    if number < 10:
        return f'0{number}'
    return f'{number}'


def get_hours_minutes_and_seconds(seconds: int) -> str:
    if seconds < 0:
        seconds += day_seconds
    elif seconds >= day_seconds:
        seconds -= day_seconds

    hours = seconds // (60 * 60)
    seconds = seconds % (60 * 60)

    minutes = seconds // 60
    seconds = seconds % 60

    return \
        f'{make_number_two_digits(hours)}:{make_number_two_digits(minutes)}:{make_number_two_digits(seconds)}'


def parse_time_to_seconds(time: str) -> int:
    h, m, s = map(int, time.split(':'))
    return get_seconds(h, m, s)


def get_pass_time(local_start_s: int, local_end_s: int) -> float:
    double_pass = local_end_s - local_start_s
    if double_pass < 0:
        double_pass += day_seconds
    return double_pass / 2


def solve_SNTP(local_start_time: str, server_time: str, local_end_time: str) -> str:
    local_start_s = parse_time_to_seconds(local_start_time)
    server_s = parse_time_to_seconds(server_time)
    local_end_s = parse_time_to_seconds(local_end_time)

    pass_time_s = get_pass_time(local_start_s, local_end_s)

    result_s = math.floor(server_s + pass_time_s + 0.5)
    return get_hours_minutes_and_seconds(result_s)


if __name__ == '__main__':
    a = input()
    b = input()
    c = input()

    print(solve_SNTP(a, b, c))
