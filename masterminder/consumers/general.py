import os

from masterminder.config import config
from masterminder.lib.broker import listen
from masterminder.lib import broker
from masterminder.consumers.pandora import current_station

###############
# App startup #
###############
@listen("app.start")
def app_start(data):

    os.system('su - pi -c "screen -dm -S pianobar pianobar"')

    broker.broadcast("pandora.station.set", current_station())

################
# Volume Stuff #
################
@listen("gpio.volume_up")
def volume_up(data):
    set_volume(current_volume() + 1)

@listen("gpio.volume_down")
def volume_down(data):
    set_volume(current_volume() - 1)

def set_volume(v):
    volumes = config['volumes']
    if v < len(volumes) and volume >= 0:
        set_to = volumes[v]
        print 'amixer set %s %s%' % (config['sound_out'], set_to)
        os.system('amixer set %s %s%' % (config['sound_out'], set_to))

def current_volume():
    try:
        with open(config['current_volume'], 'r') as f:
            return int(f.read().replace('\n', ''))
    except:
	    return 1
