def get_max_string_prettiness(change_count: int, string: str) -> int:
    letters_dict = {}
    res = 0
    start = 0
    one_letters_in_window_count = 0
    for end in range(len(string)):
        letter = string[end]
        if letter not in letters_dict:
            letters_dict[letter] = 0
        letters_dict[letter] += 1
        one_letters_in_window_count = max(one_letters_in_window_count, letters_dict[letter])
        if end - start - one_letters_in_window_count + 1 > change_count:
            letters_dict[string[start]] -= 1
            start += 1
        res = max(res, end - start + 1)

    return res


if __name__ == '__main__':
    k = int(input())
    s = input()

    print(get_max_string_prettiness(k, s))
