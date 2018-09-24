from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class UDPServer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 1234

        self.transport.connect(host, port)
        print("now we can only send to host %s port %d" % (host, port))
        #self.transport.write("UDP Server Online")

    def datagramReceived(self, data, address):

        print("received %r from %s" % (data, address))

        self.transport.write(b"response back from server")

        print("Hello was sent back to server")


    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")


reactor.listenUDP(1233, UDPServer())
reactor.run()
