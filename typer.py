from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

long = float(input("How much time do you need(in seconds)? "))

word = input("What sentence do you want to type? ")

time.sleep(long)
for char in word:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.1)
