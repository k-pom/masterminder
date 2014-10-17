import multiprocessing
from masterminder.lib import broker
class Input(object):

    def listen(self):
        """
            This will monitor to see if the current input has an
            event that should be broadcast. If so, fork and let
            the broker know about it.

            This should be called in a while(True) loop or
            equivalent
        """
        data = self.check()
        if(data):
            p = multiprocessing.Process(
                target=broker.handle_message,
                args=(self.name, data)
            )
            p.start()
            return True
