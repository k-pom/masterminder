
handlers = []

def handle_message(event_name, data):
    print "Event triggered: %s" % event_name
    print data
    print "******"

    for handler in handlers:
        if handler["listen_on"] == event_name:
            handler["handler"](data)

def register_consumer(listen_on, handler):
    handlers.append({
        "listen_on": listen_on,
        "handler": handler
    })


# This should be in masterminder.consumers.sample
def sample_consumer(data):
    print "CONSUMING DATA"
    print data

# This should be in main.py
register_consumer("fifodata", sample_consumer)
