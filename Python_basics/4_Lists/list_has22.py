def has22(nums):
    """
    (list of integers) -->  Bool
    A function that accepts a list of integer and return True/False based on if the array has a 2 next to 2.
    >>>has22([1, 2, 2]) → True
    >>>has22([1, 2, 1, 2]) → False
    >>>has22([2, 1, 2]) → False
    """
    for idx in range(len(nums) - 1):
        if nums[idx] == 2 and nums[idx + 1] == 2:
            return True

    return False


print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))
