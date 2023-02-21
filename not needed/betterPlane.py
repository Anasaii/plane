
from threading import Thread
import keyboard

speed = 0.05
def check():
    i = input()
    global speed
    speed = 0

Thread(target = check).start()

import sys, time, random, os
from colored import fg
import msvcrt

blue = fg('blue')
red = fg('red')
normal = fg('orchid_2')
white = fg('white')
magenta = fg('magenta')
gold = fg("gold_1")
green = fg("green")


def clearCMDTEXT():
    os.system('cls' if os.name == 'nt' else 'clear')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(speed)




slowprint("Type something here slowly")