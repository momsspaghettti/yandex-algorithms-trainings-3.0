close_to_open_brackets = {
    ')': '(',
    ']': '[',
    '}': '{'
}


def is_open_bracket(bracket: str) -> bool:
    return bracket == '(' or bracket == '[' or bracket == '{'


def get_open_bracket(close_bracket: str) -> str:
    return close_to_open_brackets[close_bracket]


def is_brackets_sequence_correct(seq: str) -> bool:
    if len(seq) == 0:
        return True

    stack = []
    for b in seq:
        if is_open_bracket(b):
            stack.append(b)
            continue
        if len(stack) == 0:
            return False
        if stack[-1] != get_open_bracket(b):
            return False
        stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    if is_brackets_sequence_correct(input()):
        print('yes')
    else:
        print('no')
