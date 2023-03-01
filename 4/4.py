from typing import List, Tuple


def get_cafe_min_cost_res(daily_costs: List[int]) -> Tuple[int, int, int, List[int]]:
    n = len(daily_costs)
    inf = 100 * 100 * 300 + 1
    dp = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    for day_num in range(1, n + 1):
        for coupon_count in range(0, n + 1):
            if coupon_count + 1 < n:
                dp[day_num][coupon_count] = min(
                    dp[day_num][coupon_count],
                    dp[day_num - 1][coupon_count + 1])

            if daily_costs[day_num - 1] > 100:
                dp[day_num][coupon_count] = min(
                    dp[day_num][coupon_count],
                    dp[day_num - 1][coupon_count - 1] + daily_costs[day_num - 1])
            else:
                dp[day_num][coupon_count] = min(
                    dp[day_num][coupon_count],
                    dp[day_num - 1][coupon_count] + daily_costs[day_num - 1])

    remaining_coupons_count = 0
    min_ = dp[n][remaining_coupons_count]
    for i in range(n + 1):
        if dp[n][i] <= min_:
            min_ = dp[n][i]
            remaining_coupons_count = i

    coupons_count = remaining_coupons_count
    spent_coupons_count = 0
    coupon_days_ = []
    for day in range(n, 1, -1):
        if coupons_count + 1 < n and \
                dp[day][coupons_count] != inf and \
                dp[day][coupons_count] == dp[day - 1][coupons_count + 1]:
            spent_coupons_count += 1
            coupon_days_.append(day)
            coupons_count += 1
            continue
        if daily_costs[day - 1] > 100 and coupons_count > 0 and \
                dp[day][coupons_count] == dp[day - 1][coupons_count - 1] + daily_costs[day - 1]:
            coupons_count -= 1

    return dp[n][remaining_coupons_count], remaining_coupons_count, spent_coupons_count, coupon_days_[::-1]


if __name__ == '__main__':
    n_ = int(input())
    min_cost, remaining_coupons, spent_coupons, coupon_days = get_cafe_min_cost_res(
        [int(input()) for _ in range(n_)]
    )

    print(min_cost)
    print(remaining_coupons, spent_coupons, end=' ')
    print()
    print(' '.join(map(str, coupon_days)))
