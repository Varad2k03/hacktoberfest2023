

def max_product_of_three(nums):
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

# Example usage:
print(max_product_of_three([-10, -10, 5, 2]))  # Should return 500
print(max_product_of_three([-1, -2, -3, 4]))  # Should return 24
