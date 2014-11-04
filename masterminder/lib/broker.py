import multiprocessing

handlers = []


def broadcast(name, data=None):
    multiprocessing.Process(
        target=handle_message,
        args=(name, data)
    ).start()


def handle_message(event_name, data):
    print "Event triggered: %s" % event_name
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

class listen(object):

    def __init__(self, event):
        self.event = event

    def __call__(self, func):
        print "Registering %s to %s" % (self.event, func)
        register_consumer(self.event, func)
        return func
