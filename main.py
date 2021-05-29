from pynput.keyboard import Listener
from pynput import keyboard
import pyautogui
import time
import datetime


def take_screenshot(key):
    if key==keyboard.Key.f2:
        screenshot = pyautogui.screenshot()
        string = str(datetime.date.today())+'  '+time.strftime("%I-%M-%S %p")
        screenshot.save(f'E:\\screenshots\\{string}.jpg')

listener = Listener(on_press=take_screenshot)
listener.start()
if __name__ == '__main__':
    while True:
        pass
