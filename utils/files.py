import time

import pyautogui


def save_file(path_to_file):
    time.sleep(2)
    pyautogui.write(path_to_file)
    pyautogui.press('enter')

