from typing import Union, List


class DequeWithErrorsHandling:
    def __init__(self):
        self.front_stack: List[int] = []
        self.back_stack: List[int] = []

    def push_front(self, num: int) -> str:
        self.front_stack.append(num)
        return 'ok'

    def push_back(self, num: int) -> str:
        self.back_stack.append(num)
        return 'ok'

    def pop_front(self) -> Union[int, str]:
        if self.size() == 0:
            return 'error'
        self.__move_from_back_to_front_if_needed()
        return self.front_stack.pop()

    def pop_back(self) -> Union[int, str]:
        if self.size() == 0:
            return 'error'
        self.__move_from_front_to_back_if_needed()
        return self.back_stack.pop()

    def front(self) -> Union[int, str]:
        if self.size() == 0:
            return 'error'
        self.__move_from_back_to_front_if_needed()
        return self.front_stack[-1]

    def back(self) -> Union[int, str]:
        if self.size() == 0:
            return 'error'
        self.__move_from_front_to_back_if_needed()
        return self.back_stack[-1]

    def size(self) -> int:
        return len(self.front_stack) + len(self.back_stack)

    def clear(self) -> str:
        self.front_stack.clear()
        self.back_stack.clear()
        return 'ok'

    def __move_from_back_to_front_if_needed(self) -> None:
        self.__move_from_to_if_needed(self.back_stack, self.front_stack)

    def __move_from_front_to_back_if_needed(self) -> None:
        self.__move_from_to_if_needed(self.front_stack, self.back_stack)

    @staticmethod
    def __move_from_to_if_needed(from_: List[int], to_: List[int]):
        if len(to_) > 0:
            return
        while len(from_) > 0:
            to_.append(from_.pop())


def process_deque_requests():
    deque = DequeWithErrorsHandling()

    one_parameters_commands = {
        'push_front': deque.push_front,
        'push_back': deque.push_back
    }

    zero_parameters_commands = {
        'pop_front': deque.pop_front,
        'pop_back': deque.pop_back,
        'front': deque.front,
        'back': deque.back,
        'size': deque.size,
        'clear': deque.clear
    }

    input_str = input()
    while input_str != 'exit':
        input_str_arr = input_str.split()
        command = input_str_arr[0]

        if command in zero_parameters_commands:
            print(zero_parameters_commands[command]())
        else:
            print(one_parameters_commands[command](int(input_str_arr[1])))

        input_str = input()

    print('bye')


if __name__ == '__main__':
    process_deque_requests()
