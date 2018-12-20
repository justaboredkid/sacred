from blessed import Terminal
from time import sleep
import json

t = Terminal()


class Scene(object):

    def __init__(self):
        self.objs = []
        self.pos = []
        self.txts = []

    def reset(self):
        self.objs.clear()
        self.pos.clear()
        self.txts.clear()

    def obj(self, file, x=0, y=0):  # loads ascii json files
        with open(file, "r") as o:
            self.objs.append(json.load(o))
            self.pos.append([x, y])
            o.seek(0)
            f = o.read()
        return f

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

    def render(self):
        i = 0
        for obj in self.objs:
            printobj(obj, self.pos[i][0], self.pos[i][1])
            i += 1

        for txt in self.txts:
            with t.location(txt[1], txt[2]):
                print(txt[0])


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
        if pos[1] + len(pos[0]) + x >= t.width:
            raise TooLarge
        with t.location(x, y + int(item)):
            print(" " * pos[1] + pos[0])


def txtbox(txt, x=0, y=t.height - 1):
    with t.location(x, y):
        i = input(txt)
        return i


def clear():  # clears screen
    print(t.clear())
