import multiprocessing
import time


def sample_consumer(data):
    name = multiprocessing.current_process().name
    print "%s : CONSUMING DATA" % name
    print data
    print time.sleep(3)
    print "%s : ALL DONE" % name
