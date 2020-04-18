import Receiver as Re
import Canal as Ca
import Emitter as Em


class Transmission:
    def __init__(self):
        self.emitter = Em.Emitter(2)
        self.canal = Ca.Canal()
        self.receiver = Re.Receiver()

    def parity_transmit(self):
        while self.receiver.get_request() == 1:
            self.emitter.parity_encode()
            signal = self.emitter.send_signal()
            self.canal.set_signal(signal)
            self.canal.noise()
            signal1 = self.canal.send_through()
            print(signal1)
            self.receiver.set_signal(signal1)
            self.receiver.parity_check()

    def crc_transmit(self):
        self.emitter.crc_encode()


a = Transmission()
#a.parity_transmit()
a.crc_transmit()
