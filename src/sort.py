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

def selection_sort(array):
  # O(N^2). Actually O(N^2/2), but Big O Notation doesn't care about constants...
  first_idx_to_sort = 0
  last_idx_to_sort = len(array)
  
  while first_idx_to_sort < last_idx_to_sort:
    idx_lowest_num = first_idx_to_sort
    for idx in range(first_idx_to_sort+1, last_idx_to_sort):
      if array[idx] < array[idx_lowest_num]:
        idx_lowest_num = idx
    array[first_idx_to_sort], array[idx_lowest_num] = array[idx_lowest_num], array[first_idx_to_sort]
    first_idx_to_sort += 1

  return array
