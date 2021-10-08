from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from datetime import date
import os
import sys
import requests

"""
TODO: This docstring will, in its completed form, contain licensing information and usage parameters.

Usage: <filename>.py <panelname> <panelname> <panelname>
eg.: sudo python3 dashboard.py clock weather calendar

Panels are generated from top to bottom, with the order matching the left-to-right order specified in your usage arguments.

MIT License? GPL? I'll have to read and determine what is most appropriate for redistribution and modification.
"""

# Count number of panels to generate:
if len(sys.argv) > 3:
    print("Too many panels. You may select up to 3.")
    exit()
elif len(sys.argv) == 0:
    print("You have not specified any panels. Please specify up to 3. Or pass the 'help' argument for additional information.")
else:
    panelCount = int(len(sys.argv))


# Defines Inky model
inky_display = InkyWHAT("yellow")
inky_display.set_border(inky_display.BLACK)

# Set parameters for font, canvas, and mechanism
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
x = 0
y = 0

# Header and body fonts
font = ImageFont.truetype(font="/usr/share/fonts/opentype/firacode/FiraCode-Regular.otf",size=36)
fontBold = ImageFont.truetype(font="/usr/share/fonts/opentype/firacode/FiraCode-Bold.otf",size=36)

#Read and return OpenWeather API Key
def getOWKey():
    f=open('owkey')
    owKey = f.read()
    f.close()
    return owKey

#Current Weather
def getCurrentWeather():
    print("TODO: FINISH THIS FUNCTION")

message = [str(date.today()),str(getCurrentWeather()),str("\[PLACEHOLDER\]")]


# Draw Separators
for i in range (1,int(panelCount)):
    draw.line([0,((inky_display.HEIGHT / 3) * i),(inky_display.WIDTH,((inky_display.HEIGHT / 3) * i))],fill=inky_display.BLACK,width=4)

#Compose Header
#for text in header:
#    print(text)
#    w, h = fontBold.getsize(text)
#    draw.text((x,y),text,inky_display.YELLOW,fontBold)
#    y += h

#Compose Body
for text in message:
    print(text)
    w, h = font.getsize(text)
    draw.text((x,y+8),text,inky_display.BLACK, font)
    y += (inky_display.HEIGHT / 3)

# Finalize and send to display
inky_display.set_image(img.rotate(180))
inky_display.show()

