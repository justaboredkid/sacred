from blessed import Terminal
from time import sleep
import os
import sys
import json
import re
# import threading

t = Terminal()
screen = []


def create_stage(w=t.width, h=t.height):
    global screen
    screen = [w * " " for i in range(0, h - 1)]


class Scene(object):

    def __init__(self):
        if screen is None:
            create_stage()

    def reset(self):
        global screen
        screen = [len(screen[0]) * " " for i in range(0, len(screen))]

    def obj(self, file, x=0, y=0):  # loads ascii json files
        global screen
        try:
            if not os.path.isabs(file):
                file = os.path.abspath(os.path.dirname(
                    sys.argv[0])) + "/" + file
            with open(file, "r") as o:
                j = json.load(o)

                for key, item in j.items():
                    if key != "size":
                        screen[y + int(key)] = screen[y + int(key)][:(
                            x + item[1])] + item[0] + screen[y + int(key)][(
                                x + (item[1] + len(item[0]))):]

                if "size" not in j.keys():  # 0.1.0 compatibility
                    s = []
                    for i in j.values():
                        s.append(len(i[0]))
                    j["size"] = [max(s), len(j)]
            return j
        except IndexError:
            raise TooLarge

    def txt(self, txt: str, x=0, y=0):
        global screen
        try:
            raw = re.sub(r"\x1b\[\d{1,3}m|\x1b\(B\x1b\[m", "", txt)  #ANSI stuff
            screen[y] = screen[y][:x] + txt + screen[y][x + len(raw):]
        except IndexError:
            raise TooLarge

    def box(self, x=0, y=0, w=t.width, h=t.height - 1, fill=" "):
        global screen
        try:
            if len(fill) > 1:
                raise ValueError  # allow only ONE char

            screen[y] = screen[y][:x] + "-" * w + screen[y][x + w:]
            screen[
                y + h -
                1] = screen[y + h - 1][:x] + "-" * w + screen[y + h - 1][x + w:]

            for i in range(0, int(h) - 2):
                screen[y + i + 1] = screen[y + i][:x] + "|" + fill * (
                    w - 2) + "|" + screen[y + i][x + w:]
        except IndexError:
            raise TooLarge

    def render(self): #for unadjusted stages. deprecated.
        global screen
        frame = "\n".join(screen) + "\n"

        sys.stdout.write(frame)


class Camera(object):
    global screen

    def move(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, x=0, y=0):
        self.move(x, y)

    def render(self):
        r = screen[self.y:self.y + t.height]
        r = [r[i][self.x:self.x + t.width] for i in range(0, len(r))]

        sys.stdout.write("\n".join(r) + "\n")

    # HOW DO YOU DO THISSSS?!?!?!??!?


class TooLarge(Exception):

    def __init__(self):
        clear()

        print(t.bold_red_on_bright_yellow("Scene exceeds terminal width"))
        print(
            t.bold_white_on_green(
                "User: If possible, maximize the terminal window.\nDev: Make sure your x values are in check."
            ))


def fill(txt, delay=0, diag=True):  # fills screen with txt
    if len(txt) > 1:
        raise ValueError  # allow only ONE char
    if diag:
        for _ in range(0, (t.height - 2)):
            print(txt * (t.width - 1))
            sleep(delay)
    else:
        for _ in range(0, t.height - 1):
            print(txt * (t.width - 1))
            sleep(delay)


def txtbox(txt, x=0, y=t.height - 1):
    with t.location(x, y):
        i = input(txt)
        return i


def clear():  # clears screen
    print((t.width * " " + "\n") * t.height)


if "__name__" == "__main__":
    print("What the heck are you doing?")