from masterminder.lib.broker import listen
from masterminder.lib.lcddriver import LCD

lcd = LCD.Instance()

@listen("app.start")
def app_start(data):

    try:
        lcd.lcd_clear()
        lcd.lcd_display_string("Starting Application", 1)

    except:
        print "IO Error (app_start)"

    # start pianobar in background

    # read /var/pandora_station

    # broadcast station select
