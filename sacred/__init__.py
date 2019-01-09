from blessed import Terminal
from time import sleep
import os
import sys
import json
# import threading

t = Terminal()
""" class mover(threading.Thread):

    def start(self):
        pass

    def run(self, x1, y1, mx, my, leng, loop):

        printobj(self.getName, x1, y1)
 """
""" def main():
    for x in range(4):
        mythread = mover(name="Thread-{}".format(x + 1))
        mythread.start() """


class Scene(object):

    def __init__(self, w=t.width, h=t.height, trpnt=True):
        self.objs = []
        self.pos = []
        self.txts = []
        self.width = w
        self.height = h

    def reset(self):
        self.objs.clear()
        self.pos.clear()
        self.txts.clear()

    def obj(self, file, x=0, y=0):  # loads ascii json files
        if not os.path.isabs(file):
            file = os.path.abspath(os.path.dirname(sys.argv[0])) + "/" + file
        with open(file, "r") as o:
            j = json.load(o)
            self.objs.append(j)

            if "size" not in j.keys():  # 0.1.0 compatibility
                s = []
                for i in j.values():
                    s.append(len(i[0]))
                j["size"] = [max(s), len(j)]

            self.pos.append([x, y])
            o.seek(0)
        return j

    def txt(self, txt, x=0, y=0):
        self.txts.append([txt, x, y])

    def box(self, x=0, y=0, w=t.width - 1, h=t.height - 1, fill=" "):
        if len(fill) > 1:
            raise ValueError  # allow only ONE char
        box = {"1": ["-" * w, 0], str(h): ["-" * w, 0]}
        if h == t.height - 1:
            for i in range(1, int(h) - 1):
                box[i] = ["|" + fill * (w - 2) + "|", 0]
        else:
            for i in range(2, int(h)):
                box[i] = ["|" + fill * (w - 2) + "|", 0]
        self.objs.append(box)
        self.pos.append([x, y])

    def render(self):  # deprecate this?
        i = 0
        for obj in self.objs:
            printobj(obj, self.pos[i][0], self.pos[i][1])
            i += 1

        for txt in self.txts:
            with t.location(txt[1], txt[2]):
                print(txt[0])


class Camera(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # HOW DO YOU DO THISSSS?!?!?!??!?


class TooLarge(Exception):

    def __init__(self):
        clear()

        print(t.bold_red_on_bright_yellow("Scene exceeds terminal width"))
        print(
            t.white_on_green(
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


def printobj(js, x, y):
    for item, pos in js.items():
        if item != "size":
            if pos[1] + len(pos[0]) + x >= t.width:
                raise TooLarge
            with t.location(x, y + int(item)):
                print(" " * pos[1] + pos[0], flush=True)


def txtbox(txt, x=0, y=t.height - 1):
    with t.location(x, y):
        i = input(txt)
        return i


def clear():  # clears screen
    print(t.clear())


if "__name__" == "__main__":
    print("What the heck are you doing?")