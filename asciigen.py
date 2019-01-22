#!/usr/bin/python3
'''

Generates json file for render.py
Note: NOT PERFECT. Adjust stuff yourself.

{"line#":["text", SpaceBeforeText]}

The actual process does not require this script, you can 
delete this if you want to.

'''
import json
import re
from sys import argv


def write():
    file = argv[2]
    if file.rfind(".json") == -1:
        file = argv[2] + ".json"

    with open(file, "w") as s:
        json.dump(obj, s)


def main():
    if len(argv) == 3:
        infile = argv[1]
        obj = {}
        with open(infile, "r") as f:
            ln = f.readlines()
            splist = [re.search(r"[^ ]", l).start() for l in ln]
            i = 1

            for l in ln:
                sp = min(s for s in splist)
                if sp > 10:
                    obj[i] = [
                        l[splist[i - 1]:].replace("\n", ""),
                        round((splist[i - 1] - sp) / 5)
                    ]  # for better spacing in terminals
                else:
                    obj[i] = [
                        l[splist[i - 1]:].replace("\n", ""),
                        (splist[i - 1] - sp)
                    ]

                i += 1
            obj["size"] = [len(max(ln, key=len)), i - 1]

        write()

    else:
        print("Usage: asciigen.py <inputfile> <outputname>")


if __name__ == "__main__":
    main()