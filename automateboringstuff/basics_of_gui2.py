import pyautogui
import time

time.sleep(5)
pyautogui.click()
distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.25)
    distance -= 50
    pyautogui.dragRel(0, distance, duration=0.25)
    pyautogui.dragRel(-distance, 0, duration=0.25)
    distance -= 50
    pyautogui.dragRel(0, -distance, duration= 0.25)

pyautogui.typewrite(['Hello World!!!', 'enter', 'This is a grey winter day!', 'left', 'left', 'have a coffee!'])

