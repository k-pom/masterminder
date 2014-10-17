import RPi.GPIO as GPIO

from masterminder.config import config

from masterminder.inputs.pin import PinInput
from masterminder.inputs.fifo import FifoInput

from masterminder.consumers import sample
from masterminder.consumers import pandora

from masterminder.lib import broker


GPIO.setmode(GPIO.BCM)

channels = []
for name, number in config['controls'].iteritems():
    channels.append(PinInput(number, name))

channels.append(FifoInput(config['input_fifo']))

# fifo event listeners
broker.register_consumer("fifo.pandora.songstart", sample.sample_consumer)

# gpio events
broker.register_consumer("gpio.pause", pandora.pause)
broker.register_consumer("gpio.skip", pandora.skip)

while True:
    for channel in channels:
        channel.listen()

GPIO.cleanup()
