import RPi.GPIO as GPIO
from masterminder.lib.input import Input


class PinInput(Input):
    def __init__(self, number, name, pull_up_down=GPIO.PUD_DOWN):
        """
            Inialize a new pin
            :param number: BCM or BOARD number
            :param name: The broadcasted event name
            :param pull_up_down: GPIO.PUD_DOWN or GPIO.PUD_UP
        """
        self.number = number
        self.pull_up_down = pull_up_down
        self.name = name

        GPIO.setup(self.number, GPIO.IN, self.pull_up_down)

    def check(self):
        """
            Check for the pin voltage and return if it is in an
            actionable state
        """
        return (GPIO.input(self.number) == self.get_closed_state)

    def get_closed_state(self):
        """
            Pull down inputs should be triggered when the circut
            is close (voltage), represented as 1.
            Pull up inputs should be triggered when the circut is
            open (no voltage), represented as 0
        """
        return 1 if self.pull_up_down == GPIO.PUD_DOWN else 0
