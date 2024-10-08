# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio
import os.path
import sys
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(sys.version)
    path=os.path.abspath(".")
    print(path)
    print(os.path.curdir)
    print(os.path.abspath(os.path.curdir))
    print(os.EX_OK)
    print(os.O_CREAT)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
