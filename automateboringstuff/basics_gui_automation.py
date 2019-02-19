import pyautogui

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

size = pyautogui.size()
print(size)
for i in range(2):
    pyautogui.moveTo(100, 500, duration=0.25)
    pyautogui.moveTo(500, 100, duration=0.25)
    pyautogui.moveTo(500, 500, duration=0.25)
    pyautogui.moveTo(100, 500, duration=0.25)

pyautogui.moveRel(0,100,duration= 0.25)
print(pyautogui.position())