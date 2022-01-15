def linear_search(array, value):
  # O(N)
  for idx, val in enumerate(array):
    if val == value:
      return idx
  return None

def binary_search(array, value):
  # O(log N) with OrderedArray
  pass

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
