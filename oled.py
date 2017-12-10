import time

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Oled:
    def __init__(self):
        self.disp = Adafruit_SSD1306.SSD1306_128_32(None)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()
        
        self.image = Image.new('1', (self.disp.width, self.disp.height))
        self.draw = ImageDraw.Draw(self.image)

        self.font = ImageFont.load_default()

        self.station = "Initializing..."
        self.info = ("", "")

    def update(self, station, info):
        if station != self.station or info != self.info:
            self.station = station
            self.info = info
            self.refresh()

    def refresh(self):
        self.draw.rectangle((0, 0, self.disp.width, self.disp.height), outline=0, fill=0)
        y = 0
        x = 0

        self.draw.rectangle((0, 0, self.disp.width, self.disp.height), outline=0, fill=0)

        self.draw.text((x, y), self.station, font=self.font, fill=255)

        if self.info[0] != None:
            self.draw.text((x, y+10), self.info[0], font=self.font, fill=255)

        if self.info[1] != None:
            self.draw.text((x, y+20), self.info[1], font=self.font, fill=255)

        self.disp.image(self.image)
        self.disp.display()
