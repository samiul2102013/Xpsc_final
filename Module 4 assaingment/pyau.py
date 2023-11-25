import pyautogui
import time

n= int(input("Enter the number of lines: "))

time.sleep(5)

line = ''
pyautogui.typewrite(str(n))
pyautogui.press('enter')
for i in range(1, n + 1):
    line+='*'
    pyautogui.typewrite(line)
    pyautogui.press('enter')
