from contextlib import contextmanager

import time
@contextmanager
def timeblock(label):
    start = time.clock()
    try:
    	yield
    finally:
        end = time.clock()
        print ('{} : {:.4f}'.format(label, end - start))


