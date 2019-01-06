# sacred-tui
ASCII art import and terminal graphics. IN PYTHON. 

![sacred library demo](demo.gif)

  Let's say you want something like this in your script:
```
 _____________________________,----,__
|==============================<| /___\          ____,-------------.____
 `------------------.-----.---.___.--'     __.--'-----------------------`--.__
                     `._   `.            =======================================
                    ____`.___`._____,----'     `--------,----------------'
                   /_|___________-----<       ========,'
                                 `-.                ,'
                                    `----.______,--'
```
*ASCII art made by Joshua Bell*  
  
And what if you wanted it at *exactly*, *precisely* 10 spaces to the right?
You can do this:
```
print("           _____________________________,----,__")
print("          |==============================<| /___\\          ____,-------------.____")
print("            `------------------.-----.---.___.--'     __.--'-----------------------`--.__")
print("                                `._   `.            =======================================")
print("                              ____`.___`._____,----'     `--------,----------------'")
print("                              /_|___________-----<       ========,'")
print("                                            `-.                ,'")
print("                                              `----.______,--'")
```
And add more spaces and `\\` and lose track of which line you added and then restart. **Eww no.**
  

Or maybe this:
```
from blessed import Terminal # pip install blessed

term = Terminal()

print(term.clear)

with open("ent_e.txt", "r") as f: # ent_e.txt contains the ascii art itself
    ent = f.readlines()

with term.location(10, 0):
    for line in ent:
        print(line)
```
Wait a minute:
```
           _____________________________,----,__

|==============================<| /___\          ____,-------------.____

 `------------------.-----.---.___.--'     __.--'-----------------------`--.__

                     `._   `.            =======================================

                    ____`.___`._____,----'     `--------,----------------'

                   /_|___________-----<       ========,'

                                 `-.                ,'

                                    `----.______,--'
```                                  
*AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA the ship is falling apart!!!!*
  

**Behold, sacred-tui.**
```
import sacred

scene = sacred.Scene()
sacred.clear()

scene.obj("ent_e.json", 10, 0) # ./asciigen.py ent_e.txt ent_e
scene.render()
```
and voilà!
```
           _____________________________,----,__
          |==============================<| /___\          ____,-------------.____
           `------------------.-----.---.___.--'     __.--'-----------------------`--.__
                               `._   `.            =======================================
                              ____`.___`._____,----'     `--------,----------------'
                             /_|___________-----<       ========,'
                                           `-.                ,'
                                              `----.______,--'
```                                            
Though you have to convert the ASCII art from txt to the json format that my script uses (by running the script in line 6), there is no hassle for just putting the spaceship a little bit more to the right. Or a bit toward the bottom. Anywhere on the terminal.

***ANYWHERE.***

And using this, you can still make complex scenes like this:
```
from blessed import Terminal
from math import floor
import sacred

scene = sacred.Scene()
t = Terminal()

# snippet from https://github.com/justaboredkid/ultimate-tic-tac-toe
sacred.clear()

scene.box()
scene.obj("objs/grid.json", floor(t.width / 2) - 12, floor(t.height / 2) - 11)
scene.txt(
    t.green("For best gameplay, use numpad and 80x24 terminal"), t.width - 49,
    t.height - 2)
scene.txt("1) Single Player", 4, 5)
scene.txt("2) Local Multiplayer", 4, 6)
scene.txt("3) Help", 4, 7)
scene.txt("4) Exit", 4, 8)
scene.txt(t.bright_yellow("Ultimate Tic Tac Toe TERMINAL EDITION"), 0, 0)
scene.render()
```
  
```
Ultimate Tic Tac Toe TERMINAL EDITION------------------------------------------
|                                                                             |
|                            . .  |  . .  |  . .                              |
|                           .|.|. | .|.|. | .|.|.                             |
|                            | |  |  | |  |  | |                              |
|   1) Single Player        .|.|. | .|.|. | .|.|.                             |
|   2) Local Multiplayer     | |  |  | |  |  | |                              |
|   3) Help                       |       |                                   |
|   4) Exit                 ------+-------+------                             |
|                            . .  |  . .  |  . .                              |
|                           .|.|. | .|.|. | .|.|.                             |
|                            | |  |  | |  |  | |                              |
|                           .|.|. | .|.|. | .|.|.                             |
|                            | |  |  | |  |  | |                              |
|                                 |       |                                   |
|                           ------+-------+------                             |
|                            . .  |  . .  |  . .                              |
|                           .|.|. | .|.|. | .|.|.                             |
|                            | |  |  | |  |  | |                              |
|                           .|.|. | .|.|. | .|.|.                             |
|                            | |  |  | |  |  | |                              |
|                                 |       |                                   |
-------------------------------For best gameplay, use numpad and 80x24 terminal
```
[![Maniacal laughter](https://media.giphy.com/media/xUPGcdeU3wvdNPa1Py/giphy.gif)](https://www.youtube.com/watch?v=gY2k8_sSTsE)



# Installation
Clone repo and install:
```
python3 setup.py install
```
or use pip:
```
pip install blessed-tui
```

*Note: does not support python2*

# Documentation
## [asciigen.py](https://github.com/justaboredkid/sacred/blob/master/asciigen.py)
Python script for generating ascii json files. All you need to do is to grab some ascii art (from the web or somewhere else), use ./asciigen.py to covert it into json, and:
```
import sacred

scene = sacred.Scene()

sacred.clear()
scene.obj("test.json", 5, 10)
scene.render()
```
Usage:
```
asciigen.py <inputfile> <outputname>
```

The data is in this format:
```
{"line#":["text", SpaceBeforeText]}
```
Where `line#` means which line it is, `text` being what is printed on the line, and `SpaceBeforeText` means the, well, space before the line.
## sacred.Scene(object)
Class for all objects in render. It has the following objects:
### Scene.obj(file, x=0, y=0)
Imports ascii json files.  Those are generated by ./asciigen.py
  

Args:
```
file (str): path to the .json file
x (int): position on the x axis
y (int): position on the y axis
```
### Scene.txt(txt, x=0, y=0)
Adds text to the position (x, y).  
  

Args:
```
txt (str): content to print at (x,y)
x (int): position on the x axis
y (int): position on the y axis
```
### Scene.box(x=0, y=0, w=t.width - 1, h=t.height - 1, fill=" ")
Adds a box on terminal. Creates a box around the terminal by default. (Note that a character on the terminal is a tall rectangle, which means that having the same height and width does not create a square.)
  
  
*Example:*
```
import sacred

scene = sacred.Scene() 

scene.box(5, 5, 10, 10, fill="*")
scene.render()
```
*Output:*
```


     ----------
     |********|
     |********|
     |********|
     |********|
     |********|
     |********|
     |********|
     |********|
     ----------

     
```
  
Args:
```
x (int): position on x axis
y (int): position on y axis
w (int): width (by char)
h (int): height (by char)
fill (str): content that fills inside box. (Will return ValueError if fill is more than one char.)
```

### Scene.render()
Prints (or render, if you prefer) all the objects added. Note that it prints in the order of the added objects, so each object acts more like a layer.
  
So if:
```
scene.box(5, 5, 10, 10, fill="*")
scene.box(6, 6, 10, 10) # the box will be filled by a space character (" ")
scene.render()
```
then this happens:
```




    ----------
    |        |
    | ----------
    | |********|
    | |********|
    | |********|
    | |********|
    | |********|
    | |********|
    --|********|
      |********|
      ----------


```

## sacred.TooLarge(Exception)
Error raised when the objects that are added are bigger than the width of the terminal itself.

So if you do this in a 80x24 terminal:
```
scene.box(0, 0, 500, 500)
scene.render()
```
then this happens:
```
Scene exceeds terminal width
User: If possible, maximize the terminal window.
Dev: Make sure your x values are in check.
Traceback (most recent call last):
  File "test.py", line 7, in <module>
    scene.render()
  File "/home/henry/Github/sacred/sacred.py", line 47, in render
    printobj(obj, self.pos[i][0], self.pos[i][1])
  File "/home/henry/Github/sacred/sacred.py", line 83, in printobj
    raise TooLarge
sacred.TooLarge
```

## sacred.fill(txt, delay=0, diag=True)
Fills screen with `txt`.

Example:
```
import sacred

scene = sacred.Scene()

sacred.clear()
sacred.fill("#")
scene.txt("IFR is foggy", y=23)
scene.render()
input()
```

Output:
```
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
IFR is foggy
```
By default, there is a space underneath the fill to accommodate for printing text for messages.

Args:
```
txt (str): Character to fill terminal. Will return ValueError if more than one char.
delay (int): Delay set for printing each line.
diag (bool):  Determines whether to put a blank line underneath the fill or not.
```
## sacred.printobj(js, x, y):
Used internally to print ascii json files. 

Args:
```
js (json): ascii json files should go here
x (int): Position on x axis
y (int): Position on y axis
```
## sacred.txtbox(txt, x=0, y=t.height - 1)
When `input()` is not enough. This is basically a moveable version of that, where you can set the position of it at anywhere.

By default, it prints from the bottom of the terminal.
## sacred.clear()
Clears terminal, for when you are too lazy to type `print(t.clear())`.

