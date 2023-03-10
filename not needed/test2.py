import threading
import time
import sys
import msvcrt
import os
from colored import fg

charColor = None
blue = fg('blue')
red = fg('red')
normal = fg('orchid_2')
white = fg('white')
magenta = fg('magenta')
gold = fg("gold_1")
green = fg("green")
pink = fg("hot_pink_2")
colors = [blue, red, normal, white, magenta, gold, green, pink]

skipFlag = False

def clearText():
    os.system('cls' if os.name == 'nt' else 'clear')


class SlowPrinter(threading.Thread):
    def __init__(self, text, speed=0.1):
        threading.Thread.__init__(self)
        self.text = text
        self.flag = False
        self.speed = speed
        self.last_char_index = -1

    def run(self):
            global skipFlag
            if skipFlag == False:
                for char in self.text:
                    if self.flag:
                        break
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    self.last_char_index += 1
                    time.sleep(self.speed)
            else:
                print("muahaha skipped")
                self.text = None
                return self.text

    def get_remaining_text(self):
        return self.text[self.last_char_index+1:]

def slowprint(text, speed=0.05):
    slow_printer = SlowPrinter(text, speed)
    slow_printer.start()

    while True:
        key = msvcrt.getch()
        if key == b'\r':
            slow_printer.flag = True
            slow_printer.join()
            print(slow_printer.get_remaining_text(), end='')
            break
        elif key == b'\x1b':
            time.sleep(0.5)
            os.startfile(sys.argv[0])
            sys.exit()
            
        elif key == b'x':
            global skipFlag
            skipFlag = True
            break


    print()


def speak(lines, color, speed=0.1):
    linesAmount = 0
    for x in lines:
        slowprint(color + lines[linesAmount] + white, speed)
        linesAmount += 1

def narSpeak(lines): speak(lines, green)
def charSpeak(lines): speak(lines, charColor)

class game(): 

    def initialize():
        clearText()

    def scene_1():
        global skipFlag
        slowprint("uhhh will this work anyway?")
        
        narStart = ['Work work...', "Angelicaaaaa!", "wooork wooork", "ELIZAAAAA","and peggy!"]
        char1 = ["The Schihler Sisters!"]            
        narEnd = ["Angelica", "Peggy", "Eliza!!!"]
        
        try:
            narSpeak(narStart)
            charSpeak(char1)
            narSpeak(narEnd)
        except Exception:
            print(red + "Scene 1 finished..." + white)
            skipFlag = False
        
    def chooseColor():
        global charColor
        charColor = input("Choose your color, brave hero: ")
        if charColor in colors:
            print("cool")
        else:
            slowprint("Color not in the list :(")
            charColor = red




print(blue)
#game.initialize()
game.scene_1()
