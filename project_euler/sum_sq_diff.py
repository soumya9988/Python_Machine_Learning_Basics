def sum_of_sq(num):
    sum_of_sq = 0
    i = 1
    while i <= num:
        sum_of_sq = sum_of_sq + i ** 2
        i = i + 1
    return  sum_of_sq

def sq_of_sum(num):
    sum_of_num = 0
    i = 1
    while i <= num:
        sum_of_num += i
        i = i + 1
    return sum_of_num ** 2

print(sq_of_sum(100) - sum_of_sq(100))