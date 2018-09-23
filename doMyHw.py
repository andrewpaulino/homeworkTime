import pyautogui as ptg
import time

def homework_function():

#add any keystroke that could be required (e.g If math based site: (i.e Numbers, decimals, etc.); If english based site: (i.e Words, Letters, periods, etc.))
    ptg.typewrite(['4','6','backspace','backspace'], interval=0.25)

while True: 
    homework_function()
    time.sleep(5)
    