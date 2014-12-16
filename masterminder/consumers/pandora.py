from masterminder.lib.broker import listen
from masterminder.config import config

@listen("gpio.station_down")
def station_down(data):
    print "Changing station down"
    s = _station()
    print "Current station %s" % s
    set_station(s - 1, True)

@listen("gpio.station_up")
def station_up(data):
    print "Changing station up"
    s = _station()
    print "Current station %s" % s
    set_station(s + 1, True)

@listen("gpio.pause")
def pause(data):
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

@listen("gpio.change_station")
def change_station(data):
    """ Depending on the inputs, we may select a random station,
        increase the station by one, or something else
    """
    _ctl("s")
    set_station(1)  # Should this be a broadcast event? probably


@listen("pandora.station.set")
def set_station(data, use_s=False):
    station = int(data)
    print "Writing %s  to file" % station
    with open(config['pandora_station'], 'w') as f:
        f.write(str(station))
    print "Changing station to %s" % station

    if use_s:
	_ctl("s%s\n" % station)
    else:
        _ctl("%s\n" % station)

@listen("fifo.pandora.songstart")
def songstart(data):
    pass

def _ctl(letter):
    with open(config['pandora_ctl'], "w") as fp:
        fp.write(str(letter))

def _station():
    try:
        with open(config['pandora_station'], 'r') as f:
            return int(f.read().replace('\n', ''))
    except:
	return 1


