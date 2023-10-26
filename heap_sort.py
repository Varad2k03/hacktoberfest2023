

# Heap Sort in Python

arr = [15,5,20,1,17,10,30]

def maxHeapify(arr, n, i):
  largest = i
  l = (2 * i) + 1 
  r = (2 * i) + 2
  while (l < n and arr[l] > arr[largest]):
    largest = l

  while (r < n and arr[r] > arr[largest]):
    largest = r

  if (largest != i):
    arr[largest],arr[i] = arr[i], arr[largest]
    maxHeapify(arr, n, largest)
  

def heapSort(arr):
  # Build Max Heap
  n = len(arr)
  for i in range(n//2, -1, -1):
    maxHeapify(arr, n, i)

  # Delete elements from maxHeap
  for i in range(n-1, 0, -1):
    # swap first with last element
    arr[0],arr[i] = arr[i],arr[0]

    # form maxheap again
    maxHeapify(arr, i, 0)


heapSort(arr)
print(arr)


