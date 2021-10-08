#! python3
import os
import sys
import requests

from os.path import dirname, basename, isfile, join

#Dynamically load panels at runtime in the ./panels/ directory

def loadPanels():
    for panel in os.listdir(os.path.dirname(__file__)):
        if module == '__init__.py' or module[-3:] != '.py':
            continue
        __import__(module[:-3], locals(),clobals())
    del module


class panels:
    def clock(timezone):
        print('this is a clock')

    def weather(location):
        print('here is the weather')

    def calendar():
        print('Here is your calendar')

    def slideshow():
        print('Can I make a slideshow???')
