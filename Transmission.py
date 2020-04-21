import Receiver as Re
import Canal as Ca
import Emitter as Em


class Transmission:
    def __init__(self):
        self.emitter = Em.Emitter()
        self.canal = Ca.Canal()
        self.receiver = Re.Receiver()

    def parity_transmit(self):  # metoda transmisji bitem parzystosci
        while self.receiver.get_request() == 1:
            print("signal =")
            print(self.emitter.signal)
            self.emitter.parity_encode()
            print("signal to send =")
            print(self.emitter.signal_to_send)
            sent_signal = self.emitter.send_signal()
            self.canal.set_signal(sent_signal)
            self.canal.noise()
            noised_signal = self.canal.send_through()
            print("noised signal =")
            print(noised_signal)
            self.receiver.set_signal(noised_signal)
            self.receiver.parity_check()
            print("\n")
        self.receiver.setRequest(1)

    def crc_transmit(self):  # metoda transmisji z kodowaniem crc
        crc = input("podaj crc(ciąg 0 i 1)")
        self.emitter.set_crc(crc)
        self.receiver.set_crc(crc)
        while self.receiver.get_request() == 1:
            self.emitter.crc_encode()
            sent_signal = self.emitter.send_signal()
            self.canal.set_signal(sent_signal)
            self.canal.noise()
            print("noised signal = ")
            print(sent_signal)
            noised_signal = self.canal.send_through()
            self.receiver.set_signal(noised_signal)
            self.receiver.crc_decode()
        self.receiver.setRequest(1)


def main():
    a = Transmission()
    print("trnasmisja bitem parzystosci:\n\n")
    a.parity_transmit()
    print("trnasmisja crc:\n\n")
    a.crc_transmit()


main()
