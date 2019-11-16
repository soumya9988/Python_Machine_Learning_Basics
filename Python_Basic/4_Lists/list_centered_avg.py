def centered_average(nums):
    """
    (list of int) --> float
    Precondition : List has a minimum size of 3
    Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except
    ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
    ignore just one copy, and likewise for the largest value. Use int division to produce the final average.

    >>>centered_average([1, 2, 3, 4, 100])
    3
    >>>centered_average([1, 1, 5, 5, 10, 8, 7])
    5
    >>>centered_average([-10, -4, -2, -4, -2, 0])
    -3

    """
    nums.sort()
    nums.pop()
    nums.pop(0)
    len_list = len(nums)
    if len_list % 2 == 0:
        mid_val = ( nums[len_list // 2 - 1] + nums[len_list // 2] ) // 2
    else:
        mid_val = nums[len_list // 2]
    return mid_val

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))

