from masterminder.config import config
from masterminder.lib.lcddriver import LCD

lcd = LCD.Instance()


def pause(data):
    _ctl("p")


def skip(data):
    _ctl("n")


def thumbs_up(data):
    _ctl("+")


def thumbs_down(data):
    _ctl("-")


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
        fp.write(letter)
