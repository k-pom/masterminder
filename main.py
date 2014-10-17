import os
import yaml
from masterminder.lib import gpio
from masterminder.lib.fifo import FifoInput


config = yaml.load(open("config.yaml", 'r'))

# Setup GPIO listeners
gpio.setup()
input_pins = []
for name, number in config['controls'].iteritems():
    input_pins.append(gpio.PinInput(number, name))

# Setup Fifo Listener
fifo = FifoInput("fifodata", config['fifo'])

while True:
    for pin in input_pins:
        pin.listen()
    fifo.listen()

gpio.cleanup()
