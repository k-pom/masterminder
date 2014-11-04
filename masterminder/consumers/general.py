from masterminder.lib.broker import listen
from masterminder.lib.lcddriver import LCD
from masterminder.lib import broker
from subprocess import call

lcd = LCD.Instance()

@listen("app.start")
def app_start(data):

    try:
        lcd.lcd_clear()
        lcd.lcd_display_string("Starting Application", 1)

    except:
        print "IO Error (app_start)"

    call(["su", "-", "pi" "-c" '"screen -dm -S pianobar pianobar"'])
    
    try:
        with open(config['pandora_station'], 'r') as f:
            station = f.read().replace('\n', '')
    except:
        station = 1
        print "No pandora station found. Defaulting to 1"

    broker.broadcast("pandora.station.set", station)
