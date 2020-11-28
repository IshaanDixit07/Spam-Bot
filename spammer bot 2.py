import pyautogui

spam = pyautogui.prompt('Enter message to spam') 
f_o_r = 1
longitude = int(pyautogui.prompt('enter how many times(remember 2 times = 1 time!!)')) 

while f_o_r < longitude: 
    f_o_r += 1
    pyautogui.typewrite(spam)
    pyautogui.press("enter")