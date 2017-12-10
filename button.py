import threading
import time
import RPi.GPIO as GPIO

class Button(threading.Thread):
    def __init__(self, pin):
        threading.Thread.__init__(self)
        self._pressed = False
        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.deamon = True
        self.prev_time = 0

        self.start()

    def run(self):

        while True:
            new_state = not( GPIO.input(self.pin) )

            if new_state and not ( self._pressed ) and ((time.time() - self.prev_time) > 2):
                self._pressed = True
                self.prev_time = time.time()

            time.sleep(0.1)
    
    def pressed(self):
        if self._pressed:
            self._pressed = False
            return True
        else:
            return False

