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
             return self.address
        else:
            print ("could not find '%s' bluetooth device nearby" % self.bt_name)
            return False

    # rfcomm server /client
    def server(self):
        server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)

        client_sock,address = server_sock.accept()
        print ("Accepted connection from ",address)

        data = client_sock.recv(1024)
        print ("received [%s]" % data)

        client_sock.close()
        server_sock.close()

    def client(self):
        bd_addr = bt.search()
        port = 1
        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((bd_addr, port))

        sock.send("hello!!")

        sock.close()

bt = bt_connection(target_name)
bt.client()

