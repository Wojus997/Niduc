import numpy as np


class Emitter:
    def __init__(self, signal):
        self.signal = signal
        self.signal = [1, 1, 1, 0, 0, 1]
        print(self.signal)

    def parity_encode(self):
        parity = 0
        for x in self.signal:
            parity += x
        if parity % 2:
            self.signal.append(1)
        else:
            self.signal.append(0)
        print(self.signal)

    def set_signal(self, signal):
        self.signal = signal

    def send_signal(self):
        return self.signal


a = Emitter(2)
a.parity_encode()
