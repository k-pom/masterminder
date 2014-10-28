import time
import RPi.GPIO as GPIO
from masterminder.inputs import Input


class PinInput(Input):
    def __init__(self, number, name, delay=1000, pull_up_down=GPIO.PUD_DOWN):
        """
            Inialize a new pin
            :param number: BCM or BOARD number
            :param name: The broadcasted event name
            :param delay: Keep from broadcasting multiple events (in ms)
            :param pull_up_down: GPIO.PUD_DOWN or GPIO.PUD_UP
        """
        self.number = number
        self.pull_up_down = pull_up_down
        self.name = name
        self.closed_state = self.get_closed_state()
        self.last_check_time = None
        self.delay = delay

        GPIO.setup(self.number, GPIO.IN, self.pull_up_down)

    def check(self):
        """
            Check for the pin voltage and return if it is in an
            actionable state
        """
        if GPIO.input(self.number) == self.closed_state:
            current_time = now_in_ms()
            if (current_time - self.last_check_time) > self.delay:
                self.last_check_time = current_time
                return True
        return False

    def get_closed_state(self):
        """
            Pull down inputs should be triggered when the circut
            is close (voltage), represented as 1.
            Pull up inputs should be triggered when the circut is
            open (no voltage), represented as 0
        """
        return 1 if self.pull_up_down == GPIO.PUD_DOWN else 0

def now_in_ms():
    return int(round(time.time() * 1000))
