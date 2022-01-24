def linear_search(array, value):
    # O(N)
    for idx, val in enumerate(array):
        if val == value:
            return idx
    return None


def binary_search(array, value):
    # O(log N) with Ordered Array
    start_idx = 0
    end_idx = len(array) - 1
    while True:
        middlepoint = end_idx - start_idx // 2
        if array[middlepoint] < value:
            start_idx = middlepoint + 1
        elif array[middlepoint] > value:
            end_idx = middlepoint - 1
        elif array[middlepoint] == value:
            return middlepoint


def has_duplicates(array):
    # O(N^2)
    for i in range(len(array)):
        for j in range(len(array)):
            if (i != j) & (array[i] == array[j]):
                return True
    return False


def greatest_number(array):
    # O(N)
    greatest_num = array[0]
    for num in array[1:]:
        if num > greatest_num:
            greatest_num = num
    return greatest_num


def intersection(array1, array2):
    # O(N)
    if array1 > array2:
        large_array = array1
        small_array = array2
    large_array = array2
    small_array = array1

    index = {}
    for char in large_array:
        index[char] = True

    intersection = []
    for char in small_array:
        if char in index:
            intersection.append(char)
    return intersection
