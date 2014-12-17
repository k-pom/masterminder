import os

from masterminder.lib.broker import listen
from masterminder.lib import broker
from masterminder.consumers.pandora import current_station

@listen("app.start")
def app_start(data):

    os.system('su - pi -c "screen -dm -S pianobar pianobar"')

    broker.broadcast("pandora.station.set", current_station())
