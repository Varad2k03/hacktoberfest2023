# Bubble Sort
# Insertion sort
# Merge Sort
# Quick Sort
# Selection sort
import random

# Bubble sort: Time Complexity O(n^2)
def bubbleSort(nums):
    # Convert input to a list
    nums = list(nums)

    # Outer loop for passes
    for i in range(len(nums)-1):
        # Inner loop for comparisons and swapping
        for j in range(len(nums)-1):
            # Compare adjacent elements
            if nums[j] > nums[j+1]:
                # Swap elements if they are out of order
                nums[j], nums[j+1] = nums[j+1], nums[j]

            # Print intermediate results (optional)
            print(i, j, nums)

    # Return the sorted list
    return nums



# Check if the the sorted array is in place or can used with list()'


# Insertion sort: Time Complexity O(n^2)
def insertionSort(nums):
    # Convert input to a list
    nums = list(nums)

    # Iterate over each element in the list
    for i in range(len(nums)):
        # Remove the current element from the list
        current_num = nums.pop(i)

        # Initialize the index of the previous element
        previous = i - 1

        # Find the correct position to insert the current element
        while previous >= 0 and nums[previous] > current_num:
            # Move the previous element to the right
            previous -= 1

        # Insert the current element at the correct position
        nums.insert(previous + 1, current_num)

    # Return the sorted list
    return nums


print(insertionSort([5,6,8,1,51,5,35,4]))


# Merge sort: Time Complexity O(n log(n))

# Merge two sorted lists
def merge(nums1, nums2):
    nums = []
    while len(nums1) > 0 and len(nums2) > 0:
        if nums1[0] >= nums2[0]:
            nums.append(nums2.pop(0))
        else:
            nums.append(nums1.pop(0))

    # Append any remaining elements from nums1 or nums2
    nums.extend(nums1 + nums2)

    return nums


# Perform merge sort
def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    # Divide the list into two halves
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    # Recursively sort the left and right halves
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)

    # Merge the sorted halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums


print(mergeSort([45,8,6451,546,87,548,4,2,7,2,85,8,4]))




# Partition the list and rearrange elements
def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1

    # Choose a random pivot index and swap with the last element
    pivot_index = random.randint(start, end)
    nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

    l = start
    r = end - 1

    # Perform partitioning
    while l <= r:
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    # Place the pivot element at its correct position
    nums[l], nums[end] = nums[end], nums[l]
    return l


# Perform quick sort
def quickSort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        # Partition the list around the pivot
        pivot = partition(nums, start, end)

        # Recursively sort the left and right subarrays
        quickSort(nums, start, pivot - 1)
        quickSort(nums, pivot + 1, end)

    return nums

print("quicksort",quickSort([45,8,6451,546,87,548,4,2,7,2,85,8,4]))


# Selection sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Find the index of the minimum element in the unsorted part of the list
        min_index = i

        # Find the index of the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element (at index i)
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
print(selection_sort([45,8,6451,546,87,548,4,2,7,2,85,8,4]))

def cyclesort(arr):
    i = 0
    while i<len(arr):
        correct = arr[i] - 1            # 1 =  the start range
        if arr[correct] != arr[i]:
            print(arr[correct],arr[i],i)
            arr[correct],arr[i]= arr[i],arr[correct]
        else:
            i += 1
    return arr



print(cyclesort([1,5,4,2,3]))


