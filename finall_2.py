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
time.sleep(2)
keyboard.press(Key.esc)
keyboard.release(Key.esc)
