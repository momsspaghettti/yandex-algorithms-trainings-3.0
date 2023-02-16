from typing import Union


class StackWithErrorsHandling:
    def __init__(self):
        self.stack = []

    def push(self, num: int) -> str:
        self.stack.append(num)
        return 'ok'

    def pop(self) -> Union[int, str]:
        if self.size() == 0:
            return 'error'
        return self.stack.pop()

    def back(self) -> Union[int, str]:
        if self.size() == 0:
            return 'error'
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

    def clear(self) -> str:
        self.stack.clear()
        return 'ok'


def process_stack_requests():
    stack = StackWithErrorsHandling()
    zero_parameters_commands = {
        'pop': stack.pop,
        'back': stack.back,
        'size': stack.size,
        'clear': stack.clear
    }

    input_str = input()
    while input_str != 'exit':
        input_str_arr = input_str.split()
        command = input_str_arr[0]

        if command in zero_parameters_commands:
            print(zero_parameters_commands[command]())
        else:
            print(stack.push(int(input_str_arr[1])))

        input_str = input()

    print('bye')


if __name__ == '__main__':
    process_stack_requests()
