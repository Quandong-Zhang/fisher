import os
import webbrowser
import keyboard
import time

def fish(url):
    webbrowser.open(url, new=1, autoraise=True)
    keyboard.wait("esc")
    os.system("taskkill /IM chrome.exe")
    time.sleep(3)
    os.system("taskkill /F /IM chrome.exe")
