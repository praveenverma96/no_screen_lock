# to stop this code simply force your cursor to the upper left corner of the screen
import os, time
# Below will install pyautogui if it haven't already
try:
    import pyautogui
except (ImportError, ModuleNotFoundError):
    os.system('python -m pip install PyAutoGUI')
    import pyautogui

while True:
    pyautogui.moveRel(200, 200 , duration= 1)
    time.sleep(2)
    pyautogui.click(button= 'right')
    pyautogui.moveRel(-200, -200 , duration= 1)
    time.sleep(2)