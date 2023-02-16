from typing import List


def is_digit(s: str) -> bool:
    if s[0] == '-':
        return s.lstrip('-').isdigit()
    return s.isdigit()


def evaluate_expression_in_postfix_notation(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if is_digit(token):
            stack.append(int(token))
            continue
        second_op, first_op = stack.pop(), stack.pop()
        res = None
        if token == '+':
            res = first_op + second_op
        elif token == '-':
            res = first_op - second_op
        elif token == '*':
            res = first_op * second_op

        if res is not None:
            stack.append(res)

    return stack[-1]


def evaluate_expression(s: str) -> int:
    return evaluate_expression_in_postfix_notation(s.strip(' ').split(' '))


if __name__ == '__main__':
    print(evaluate_expression(input()))
