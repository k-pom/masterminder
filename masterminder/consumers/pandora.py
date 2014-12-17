import os

from masterminder.lib.broker import listen
from masterminder.lib import broker
from masterminder.config import config

@listen("gpio.station_down")
def station_down(data):
    s = current_station()
    _ctl("s")
    broker.broadcast("pandora.station.set", s - 1)

@listen("gpio.station_up")
def station_up(data):
    s = current_station()
    _ctl("s")
    broker.broadcast("pandora.station.set", s + 1)

@listen("gpio.pause")
def pause(data):
    print "Pausing..."
    _ctl("p")

@listen("gpio.skip")
def skip(data):
    _ctl("n")

@listen("gpio.like")
def thumbs_up(data):
    _ctl("+")

@listen("gpio.dislike")
def thumbs_down(data):
    _ctl("-")

@listen("pandora.station.set")
def set_station(data):
    station = int(data)
    with open(config['pandora_station'], 'w') as f:
        f.write(str(station))
    _ctl("%s\n" % station)


def _ctl(letter):

    with open(config['pandora_ctl'], "w") as fp:
        fp.write(str(letter))

def current_station():
    try:
        with open(config['pandora_station'], 'r') as f:
            return int(f.read().replace('\n', ''))
    except:
	    return 0
