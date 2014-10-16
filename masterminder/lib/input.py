
class Input(object):

    def listen(self):
        """
            This will monitor to see if the current input has an
            event that should be broadcast. If so, broadcast it.
            This should be called in a while(True) loop or
            equivalent
        """
        data = self.check()
        if(data):
            return self.broadcast(data)

    def broadcast(self, data):
        """
            Broadcast the event so other processes can pick it up
        """
        # generate message id
        # add message_id to redis
        # add message_id to the array
        print "EVENT: %s" % self.name
        print data
        return "abc-123"
