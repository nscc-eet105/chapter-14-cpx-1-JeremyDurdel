#Jeremy Durdel
#Chapter 14 CPX 1
#07/13/2025

import time
from adafruit_circuitplayground import cp

notes_dict = {
    "A4": 440,
    "B4": 494,
    "C5": 523,
    "D5": 587
}

colors = {
    "cyan": (0, 255, 255),
    "purple": (255, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "black": (0, 0, 0)
}

def fill_pixels(color_tuple):
    cp.pixels.fill(color_tuple)

while True:
    if cp.touch_A1:
        cp.start_tone(notes_dict["A4"])
        fill_pixels(colors["cyan"])
    elif cp.touch_A2:
        cp.start_tone(notes_dict["B4"])
        fill_pixels(colors["purple"])
    elif cp.touch_A3:
        cp.start_tone(notes_dict["C5"])
        fill_pixels(colors["green"])
    elif cp.touch_A4:
        cp.start_tone(notes_dict["D5"])
        fill_pixels(colors["yellow"])
    else:
        cp.stop_tone()
        fill_pixels(colors["black"])

    time.sleep(0.1)
