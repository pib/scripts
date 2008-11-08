#!/usr/bin/env python

## Config: change these to match your setup
mpd_host = 'localhost'
mpd_port = 6600

import mpd
import random

class Shuffler:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = False
        self.client = mpd.MPDClient()

    def connect(self):
        if self.connected: return
        self.client.connect(self.host, self.port)
        self.connected = True

    def disconnect(self):
        if not self.connected: return
        self.client.disconnect()
        self.connected = false

    def shuffle_rest(self):
        self.connect()
        status = self.client.status()
        self.shuffle_range(int(status['song'])+1 or 0, 
                           int(status['playlistlength'])-1)

    def shuffle_range(self, start, end):
        start, end = int(start), int(end)
        self.connect()

        for fromi in range(start, end+1):
            toi = random.randint(start, end)
            self.client.swap(fromi, toi)

if __name__=="__main__":
    import sys

    usage = """Usage: %s (rest | start end)
	rest - shuffle all the songs after the current one
	start - start of shuffling range
	end - end of shuffling range""" % (sys.argv[0])    

    if len(sys.argv) > 1:
        shuffler = Shuffler(mpd_host, mpd_port)
        if sys.argv[1] == 'rest':
            shuffler.shuffle_rest()
        elif len(sys.argv) == 3:
            shuffler.shuffle_range(sys.argv[1], sys.argv[2])

        else: print usage

    else:
        print usage
