__author__ = 'dako'

import bluetooth

target_name = "Dako HTC"

class bt_connection():
    def __init__(self, btname):
        self.address = None
        self.bt_name = btname

    def search(self):
        nearby_devices = bluetooth.discover_devices()
        for bdaddr in nearby_devices:
            if self.bt_name == bluetooth.lookup_name( bdaddr ):
                self.address = bdaddr
                break
        if self.address is not None:
             print ("found '%s' bluetooth device with address %s" % (self.bt_name, self.address))
        else:
            print ("could not find '%s' bluetooth device nearby" % self.bt_name)

bt = bt_connection(target_name)
bt_client = bt.search()
