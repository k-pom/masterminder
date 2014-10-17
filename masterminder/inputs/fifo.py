import io
import os
import json
import errno
from masterminder.inputs import Input


class FifoInput(Input):

    def __init__(self, fifo):
        try:
            os.mkfifo(fifo)
        except:
            # TODO: Check for the relevant exception type
            pass  # fifo is likely already created

        self.name = "fifo"
        self.fifo = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)

    def check(self):
        try:
            # TODO: Parse the line to get a message name and data
            line = os.read(self.fifo, io.DEFAULT_BUFFER_SIZE)
            if not line:
                return False
            try:
                data = json.loads(line)

                if "event" not in data or "data" not in data:
                    print "JSON Payload was not formatted properly."
                    print data

                self.name = "fifo.%s" % data['event']
                return data['data']
            except:
                print "input.fifo had non-json data"
                print line
                return False
        except OSError as err:
            if err.errno == errno.EAGAIN or err.errno == errno.EWOULDBLOCK:
                return False
            else:
                raise
