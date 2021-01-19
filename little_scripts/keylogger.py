import time
import logging
from pynput import mouse,keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import *

 # mouse = Controller()
# print('pointer position is {}'.format(mouse.position))
#
# mouse.position = (110,110)
#
# print('pointer position is {}'.format(mouse.position))
#
# time.sleep(2)
# mouse.move(120,120)
#
# mouse.press(Button.left)
# mouse.click(Button.left,2)



# class MyException(Exception): pass
#
# def on_click(x, y, button, pressed):
#     if button == mouse.Button.left:
#         raise MyException(button)
#
# # Collect events until released
# with mouse.Listener(
#         on_click=on_click) as listener:
#     try:
#         listener.join()
#     except MyException as e:
#         print('{0} was clicked'.format(e.args[0]))
# The event listener will be running in this block
# with mouse.Events() as events:
#     for event in events:
#         if event.button == mouse.Button.right:
#             break
#         else:
#             print('Received event {}'.format(event))
keyboard = Controller()

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
# keyboard.press('a')
# keyboard.release('a') AB

# Type two upper case As
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.alt): A
    keyboard.press('e')
    keyboard.release('b')

# Type 'Hello World' using the shortcut type method
# keyboard.type('Hello World')