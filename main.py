import RPi.GPIO as GPIO

from masterminder.config import config

from masterminder.inputs.pin import PinInput
from masterminder.inputs.fifo import FifoInput

# import these, even though they are not used, so that the
# functions can register themselves to listen for events
from masterminder.consumers import *

from masterminder.lib import broker


GPIO.setmode(GPIO.BCM)

channels = []
for name, number in config['controls'].iteritems():
    channels.append(PinInput(number, name))

channels.append(FifoInput(config['input_fifo']))

broker.broadcast("app.start")

print "Listening on all channels"
while True:
    for channel in channels:
        channel.listen()

GPIO.cleanup()
