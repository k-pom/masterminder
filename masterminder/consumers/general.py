import os

from masterminder.lib.broker import listen
from masterminder.lib import broker

@listen("app.start")
def app_start(data):

    os.system('su - pi -c "screen -dm -S pianobar pianobar"')

    try:
        with open(config['pandora_station'], 'r') as f:
            station = f.read().replace('\n', '')
    except:
        station = 1
        print "No pandora station found. Defaulting to 1"

    broker.broadcast("pandora.station.set", station)
