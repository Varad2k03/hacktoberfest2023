def linear_search(list1, key):
  """Searches for a given element in a list using linear search.

  Args:
    list1: A list of elements.
    key: The element to search for.

  Returns:
    The index of the element in the list if it is found, or -1 if it is not found.
  """

  for i in range(len(list1)):
    if list1[i] == key:
      return i
  return -1


def binary_search(list1, key):
  """Searches for a given element in a sorted list using binary search.

  Args:
    list1: A sorted list of elements.
    key: The element to search for.

  Returns:
    The index of the element in the list if it is found, or -1 if it is not found.
  """

  low = 0
  high = len(list1) - 1

  while low <= high:
    mid = (low + high) // 2
    if list1[mid] == key:
      return mid
    elif list1[mid] < key:
      low = mid + 1
    else:
      high = mid - 1

  return -1


# Example usage:

list1 = [1, 2, 3, 4, 5]

# Linear search
index = linear_search(list1, 3)
if index != -1:
  print(f"Found element {3} at index {index}.")
else:
  print(f"Element {3} not found in the list.")

# Binary search
index = binary_search(list1, 3)
if index != -1:
  print(f"Found element {3} at index {index}.")
else:
  print(f"Element {3} not found in the list.")
