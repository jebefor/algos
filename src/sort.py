def bubble_sort(array):
  # O(N^2)
  sorted = False
  last_index_to_sort = len(array) - 1
  while not sorted:
    sorted = True
    for idx in range(last_index_to_sort):
        if array[idx] > array[idx+1]:
          array[idx], array[idx+1] = array[idx+1], array[idx]
          sorted = False
    last_index_to_sort -= 1

  return array


