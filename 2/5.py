from typing import List


def heapify(arr: List[int]):
    if len(arr) < 2:
        return
    i = len(arr) // 2 - 1
    while i > -1:
        sift_down(arr, i, len(arr))
        i -= 1


def swap(arr: List[int], i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def sift_down(arr: List[int], i: int, n: int):
    l_child = i * 2 + 1
    r_child = i * 2 + 2
    if l_child >= n and r_child >= n:
        return

    if l_child < n:
        if r_child < n:
            if arr[i] >= arr[l_child] and arr[i] >= arr[r_child]:
                return
            if arr[i] < arr[l_child]:
                if arr[i] < arr[r_child]:
                    if arr[l_child] < arr[r_child]:
                        swap(arr, i, r_child)
                        sift_down(arr, r_child, n)
                    else:
                        swap(arr, i, l_child)
                        sift_down(arr, l_child, n)
                else:
                    swap(arr, i, l_child)
                    sift_down(arr, l_child, n)
            else:
                swap(arr, i, r_child)
                sift_down(arr, r_child, n)
        else:
            if arr[i] < arr[l_child]:
                swap(arr, i, l_child)
                sift_down(arr, l_child, n)
    else:
        if arr[i] < arr[r_child]:
            swap(arr, i, r_child)
            sift_down(arr, r_child, n)


def sort(arr: List[int]):
    heapify(arr)
    for i in range(len(arr) - 1, -1, -1):
        swap(arr, i, 0)
        sift_down(arr, 0, i)


if __name__ == '__main__':
    input()
    a = list(map(int, input().split(' ')))
    sort(a)
    for n in a:
        print(n, end=' ')
