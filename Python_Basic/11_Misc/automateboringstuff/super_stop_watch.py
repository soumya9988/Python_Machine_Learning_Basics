import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
start_time = time.time()
last_time = start_time
lap_no = 1

try:
    while True:
        input()
        current_time = time.time()
        lap_time = current_time - last_time
        total_time = current_time - start_time
        print('Lap#: %s, Total time : %s (%s)' % (lap_no, total_time, lap_time))
        lap_no += 1
        last_time = current_time

except KeyboardInterrupt as ex:
    print('\nDone')



