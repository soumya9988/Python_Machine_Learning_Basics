import pyautogui

pyautogui.FAILSAFE = True

print('Press Control+ C to quit')
try:
    while True:
        x_c, y_c = pyautogui.position()
        position_str = 'X Coordinate: ' + str(x_c) + ' & Y Coordinate: ' + str(y_c)
        print(position_str, end='')
        print('\b' * len(position_str), end='',  flush=True)


except KeyboardInterrupt:
    print('\nDone.')

