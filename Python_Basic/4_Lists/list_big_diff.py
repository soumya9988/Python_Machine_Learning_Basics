def big_diff(nums):
    """
    (list of int) --> int
    Function that accepts a list of numbers & return the difference between the largest and smallest values in the list
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([7, 2, 10, 9])
    8
    >>> big_diff([2, 10, 7, 2])
    8
    """
    return max(nums) - min(nums)

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))
