import multiprocessing

handlers = []


def handle_message(event_name, data):
    print "Event triggered: %s" % event_name
    print data
    print "******"

    for handler in handlers:
        if handler["listen_on"] == event_name:
            multiprocessing.Process(
                target=handler["handler"],
                args=(data,)
            ).start()


def register_consumer(listen_on, handler):
    handlers.append({
        "listen_on": listen_on,
        "handler": handler
    })
