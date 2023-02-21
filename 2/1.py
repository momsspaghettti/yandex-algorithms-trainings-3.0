from typing import Union


class QueueWithErrorsHandling:
    def __init__(self):
        self.front_stack = []
        self.back_stack = []

    def push(self, num: int) -> str:
        self.back_stack.append(num)
        return 'ok'

    def pop(self) -> Union[int, str]:
        if self.size() == 0:
            return 'error'
        self.__move_from_back_to_front_if_needed()
        return self.front_stack.pop()

    def front(self) -> Union[int, str]:
        if self.size() == 0:
            return 'error'
        self.__move_from_back_to_front_if_needed()
        return self.front_stack[-1]

    def size(self) -> int:
        return len(self.front_stack) + len(self.back_stack)

    def clear(self) -> str:
        self.front_stack.clear()
        self.back_stack.clear()
        return 'ok'

    def __move_from_back_to_front_if_needed(self) -> None:
        if len(self.front_stack) > 0:
            return
        while len(self.back_stack) > 0:
            self.front_stack.append(self.back_stack.pop())


def process_queue_requests():
    queue = QueueWithErrorsHandling()
    zero_parameters_commands = {
        'pop': queue.pop,
        'front': queue.front,
        'size': queue.size,
        'clear': queue.clear
    }

    input_str = input()
    while input_str != 'exit':
        input_str_arr = input_str.split()
        command = input_str_arr[0]

        if command in zero_parameters_commands:
            print(zero_parameters_commands[command]())
        else:
            print(queue.push(int(input_str_arr[1])))

        input_str = input()

    print('bye')


if __name__ == '__main__':
    process_queue_requests()
