import io
import os
import errno
from masterminder.lib.input import Input


class FifoInput(Input):

    def __init__(self, name, fifo):
        try:
            os.mkfifo(fifo)
        except:
            # TODO: Check for the relevant exception type
            pass  # fifo is likely already created

        self.name = name
        self.fifo = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)

    def check(self):
        try:
            # TODO: Parse the line to get a message name and data
            line = os.read(self.fifo, io.DEFAULT_BUFFER_SIZE)
        except OSError as err:
            if err.errno == errno.EAGAIN or err.errno == errno.EWOULDBLOCK:
                return False
            else:
                raise

        return line
