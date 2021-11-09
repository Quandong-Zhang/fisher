import os
import webbrowser
import keyboard
#import time


webbrowser.open("https://www.bilibili.com/bangumi/play/ss39424?t=246", new=1)
keyboard.wait("alt")
os.system("taskkill /IM chrome.exe")
#time.sleep(2.5)
#os.system("taskkill /F /IM chrome.exe")
