from pynput.keyboard import Key,Controller

import time
time.sleep(6)
keyboard=Controller()
keyboard.press(Key.ctrl)
keyboard.press("t")
keyboard.release(Key.ctrl)
keyboard.release('t')
time.sleep(3)


keyboard.press(Key.ctrl)
keyboard.press('l')
keyboard.release('l')
keyboard.release(Key.ctrl)
keyboard.type('https://cryptobrowser.site/login/google-oauth2/')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.type('bs.mojtabaebrahimi')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)

keyboard.type('9712102450')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)

keyboard.press(Key.ctrl)
keyboard.press('l')
keyboard.release('l')
keyboard.release(Key.ctrl)
keyboard.type('chrome-extension://fcaacbfglejpnljiiokpcplbmmlbmnbk/tab.html')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
