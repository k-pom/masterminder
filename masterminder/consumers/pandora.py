from masterminder.lib.broker import listen
from masterminder.config import config
from masterminder.lib.lcddriver import LCD

lcd = LCD.Instance()


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
def set_station(data):
    station = int(data)
    with open(config['pandora_station'], 'w') as f:
        f.write(str(station))
    _ctl("%s\n" % station)

@listen("fifo.pandora.songstart")
def songstart(data):

    try:
        lcd.lcd_clear()
        lcd.lcd_display_string(data["title"], 1)
        lcd.lcd_display_string(" by %s" % data["artist"], 2)
        # os.system("mpg123 'http://translate.google.com:80/translate_tts?ie=UTF-8&tl=en&q=Now playing %s by %s'" % (title[0], artist[0]))
    except:
        print "IO ERROR!"


def _ctl(letter):
    with open(config['pandora_ctl'], "w") as fp:
        fp.write(str(letter))
