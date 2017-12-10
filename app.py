from player import Player
from button import Button
from oled import Oled
from time import sleep

PIN_UP = 17
PIN_DOWN = 27

button_up = Button(PIN_UP)
button_down = Button(PIN_DOWN)

player = Player()
player.start()

oled = Oled()

while True:
    oled.update(player.get_station(), player.get_info())

    if (button_up.pressed()):
        player.up()

    if (button_down.pressed()):
        player.down()

    sleep(1)