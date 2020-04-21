import numpy as np


def xor(a, b):
    if int(a) == int(b):
        return 0
    else:
        return 1


class Emitter:
    def __init__(self):  # inicjalizacja zmiennych emitera
        self.signal = []
        self.signal = input("podaj sygnal")
        int_cast = []
        for i in range(0, len(self.signal)):
            int_cast.append(int(self.signal[i]))
        self.signal = int_cast.copy()
        self.signal_to_send = []
        self.crc = []

    def parity_encode(self):  # metoda kodowania bitem parzystosci
        parity = 0
        self.signal_to_send = self.signal.copy()
        for x in self.signal:  # liczenie sumy sygnalu
            parity += x
        if parity % 2:
            self.signal_to_send.append(1)
        else:
            self.signal_to_send.append(0)

    def crc_encode(self):  # metoda kodujaca crc
        self.signal_to_send = self.signal.copy()
        for i in range(0, len(self.crc) - 1):
            self.signal_to_send.append(0)
        print("signal = ")
        print(self.signal_to_send)
        helper = self.signal_to_send.copy()
        for i in range(0, len(self.signal)):  # podwojna petla realizująca xorowanie odpowiednich pozycji
            if int(helper[i]) == 1:
                for u in range(0, len(self.crc)):
                    num = xor(helper[u + i], self.crc[u])
                    helper[u + i] = num
        print("crc = ")
        print(helper)  # wyswietlanie crc
        for i in range(0, len(self.signal_to_send)):
            self.signal_to_send[i] = self.signal_to_send[i] + helper[i]
        print("combined")
        print(self.signal_to_send)  # wyswietlanie sygnalu po zlaczeniu z crc

    def set_signal(self, signal):
        self.signal = signal

    def send_signal(self):
        return self.signal_to_send

    def set_crc(self, crc):
        self.crc = crc

    def get_crc(self):
        return self.crc
