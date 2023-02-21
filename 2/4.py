class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, num: int) -> None:
        self.heap.append(num)
        self.__sift_up(len(self.heap) - 1)

    def extract(self) -> int:
        self.__swap(0, len(self.heap) - 1)
        res = self.heap.pop()
        self.__sift_down(0)
        return res

    def __swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __sift_up(self, i) -> None:
        if i == 0:
            return
        parent = (i - 1) // 2
        if self.heap[parent] > self.heap[i]:
            return
        self.__swap(i, parent)
        self.__sift_up(parent)

    def __sift_down(self, i: int):
        n = len(self.heap)
        l_child = i * 2 + 1
        r_child = i * 2 + 2
        if l_child >= n and r_child >= n:
            return

        if l_child < n:
            if r_child < n:
                if self.heap[i] >= self.heap[l_child] and self.heap[i] >= self.heap[r_child]:
                    return
                if self.heap[i] < self.heap[l_child]:
                    if self.heap[i] < self.heap[r_child]:
                        if self.heap[l_child] < self.heap[r_child]:
                            self.__swap(i, r_child)
                            self.__sift_down(r_child)
                        else:
                            self.__swap(i, l_child)
                            self.__sift_down(l_child)
                    else:
                        self.__swap(i, l_child)
                        self.__sift_down(l_child)
                else:
                    self.__swap(i, r_child)
                    self.__sift_down(r_child)
            else:
                if self.heap[i] < self.heap[l_child]:
                    self.__swap(i, l_child)
                    self.__sift_down(l_child)
        else:
            if self.heap[i] < self.heap[r_child]:
                self.__swap(i, r_child)
                self.__sift_down(r_child)


def process_heap_queries():
    heap = MaxHeap()

    n = int(input())
    for _ in range(n):
        inp = input().split(' ')
        if inp[0] == '0':
            heap.insert(int(inp[1]))
        elif inp[0] == '1':
            print(heap.extract())


if __name__ == '__main__':
    process_heap_queries()
