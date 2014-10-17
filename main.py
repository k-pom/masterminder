import yaml
import RPi.GPIO as GPIO
from masterminder.inputs.pin import PinInput
from masterminder.inputs.FifoInput import FifoInput
from masterminder.consumers import sample
from masterminder.lib import broker


config = yaml.load(open("config.yaml", 'r'))

GPIO.setmode(GPIO.BCM)

channels = []
for name, number in config['controls'].iteritems():
    channels.append(PinInput(number, name))

channels.append(FifoInput("fifodata", config['fifo']))

broker.register_consumer("fifodata", sample.sample_consumer)

while True:
    for channel in channels:
        channel.listen()

GPIO.cleanup()
