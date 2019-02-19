import time
import datetime


def calc_sum():
    sum_no = 0
    for i in range(1, 100001):
        sum_no += i
    return sum_no


start_time = time.time()
prod = calc_sum()
end_time = time.time()
diff_time = end_time - start_time
print('Time taken to calculate the sum is', diff_time)
print('Sum of first 100000 numbers is', prod)

# Examples of datetime
print('Date time:', datetime.datetime.now())
print(datetime.datetime.fromtimestamp(time.time()))

# Datetime object
new_year_2019 = datetime.datetime(2019, 1, 1, 0, 0, 0)
halloween_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
print(halloween_2019 - new_year_2019)

# Examples of time delta object
delta_time = datetime.timedelta(days=11, hours= 10, minutes= 9, seconds= 8, milliseconds= 7, microseconds= 6)
print(delta_time.total_seconds())
print(delta_time.seconds)
print(str(delta_time))

for i in range(1,8):
    print(datetime.datetime.now() + datetime.timedelta(days=i))

born_day = datetime.datetime(2015, 11, 25, 12, 28, 00)
thousand_day = born_day + datetime.timedelta(days=1000)
print(thousand_day)

# Convert the date time object to a string format
print(thousand_day.strftime('%d-%B-%Y, %j'))
# Convert a date string to datetime object
print(datetime.datetime.strptime('21-August-2018, 233', '%d-%B-%Y, %j'))