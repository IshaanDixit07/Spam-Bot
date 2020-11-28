import pyautogui
#You may have to import this.

spam = pyautogui.prompt('Enter message to spam') #Tell the message
f_o_r = 1 #Let this be 1 otherwise it wont stop!!
longitude = int(pyautogui.prompt('enter how many times(remember 2 times = 1 time!!)')) 

while f_o_r < longitude: 
    f_o_r += 1
    pyautogui.typewrite(spam)
    pyautogui.press("enter")
