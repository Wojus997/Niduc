import numpy as np


def xor(a, b):
    if int(a) == int(b):
        return 0
    else:
        return 1


class Emitter:
    def __init__(self, signal):
        self.signal = signal
        self.signal = [1, 1, 1, 0, 0, 1]
        self.signal_to_send = self.signal
        print(self.signal)

    def parity_encode(self):
        parity = 0
        self.signal_to_send = self.signal.copy()
        for x in self.signal:
            parity += x
        if parity % 2:
            self.signal_to_send.append(1)
        else:
            self.signal_to_send.append(0)
        # print(self.signal)

    def crc_encode(self):                   #metoda kodujaca crc
        x = input("podaj crc\n")
        self.signal_to_send = self.signal.copy()

        for i in range(0, len(x)-1):
            self.signal_to_send.append(0)
        print(self.signal_to_send)
        helper = self.signal_to_send.copy()
        for i in range(0, len(self.signal)):

            if int(helper[i]) == 1:
                for u in range(0, len(x)):
                    num = xor(helper[u+i], x[u])
                    helper[u+i]=num
        print(helper)                               #wyswietlanie crc
        for i in range(0, len(self.signal_to_send)):
            self.signal_to_send[i] = self.signal_to_send[i]+helper[i]
        print(self.signal_to_send)                #  wyswietlanie sygnalu po zlaczeniu z crc

    def set_signal(self, signal):
        self.signal = signal

    def send_signal(self):
        return self.signal_to_send
