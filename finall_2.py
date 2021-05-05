from pynput.keyboard import Key,Controller
keyboard=Controller()
import time
time.sleep(10)

keyboard.press(Key.ctrl)
keyboard.press("t")
keyboard.release(Key.ctrl)
keyboard.release('t')
time.sleep(4)


keyboard.press(Key.ctrl)
keyboard.press('l')
keyboard.release('l')
keyboard.release(Key.ctrl)
time.sleep(0.1)
keyboard.type('https://cryptobrowser.site/login/google-oauth2/')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(4)



keyboard.type('bs.mojtabaebrahimi')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)

keyboard.type('9712102450')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(3)
from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position=(372, 378)
mouse.press(Button.left)
mouse.release(Button.left)
mouse.position=(192,360)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(1)
from pynput.keyboard import Key,Controller
keyboard=Controller()
keyboard.type('eshaghnioton1999@gmail.com')
time.sleep(3)
from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position=(422,233)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(0.5)
mouse.position=(515,224)
mouse.press(Button.left)
mouse.release(Button.left)

from pynput.keyboard import Key,Controller
keyboard=Controller()
keyboard.press(Key.ctrl)
keyboard.press('t')
keyboard.release('t')
keyboard.release(Key.ctrl)


time.sleep(1)

keyboard.press(Key.ctrl)
keyboard.press('l')
keyboard.release('l')
keyboard.release(Key.ctrl)
time.sleep(0.1)
keyboard.type('chrome-extension://fcaacbfglejpnljiiokpcplbmmlbmnbk/tab.html')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(7)
from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position=(515,224)
mouse.press(Button.left)
mouse.release(Button.left)
