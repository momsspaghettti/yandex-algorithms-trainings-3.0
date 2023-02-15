from typing import List, Tuple


class SumInMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = SumInMatrix.__build_sum_matrix(matrix)

    def calc_rectangle_sum(self, left_corner: Tuple[int, int], right_corner: Tuple[int, int]) -> int:
        return \
                self.__get_sum_in_rectangle(self.sum_matrix, (right_corner[0] - 1, right_corner[1] - 1)) - \
                self.__get_sum_in_rectangle(self.sum_matrix, (right_corner[0] - 1, left_corner[1] - 2)) - \
                self.__get_sum_in_rectangle(self.sum_matrix, (left_corner[0] - 2, right_corner[1] - 1)) + \
                self.__get_sum_in_rectangle(self.sum_matrix, (left_corner[0] - 2, left_corner[1] - 2))

    @staticmethod
    def __get_sum_in_rectangle(matrix: List[List[int]], corner: Tuple[int, int]) -> int:
        i = corner[0]
        j = corner[1]
        if i < 0 or j < 0:
            return 0
        return matrix[i][j]

    @staticmethod
    def __build_sum_matrix(matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] += \
                    SumInMatrix.__get_sum_in_rectangle(matrix, (i - 1, j)) + \
                    SumInMatrix.__get_sum_in_rectangle(matrix, (i, j - 1)) - \
                    SumInMatrix.__get_sum_in_rectangle(matrix, (i - 1, j - 1))
        return matrix


def solve_sum_in_rectangle():
    n, _, k = map(int, input().split())

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    sum_in_matrix = SumInMatrix(matrix)
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        print(sum_in_matrix.calc_rectangle_sum((x1, y1), (x2, y2)))


if __name__ == '__main__':
    solve_sum_in_rectangle()
