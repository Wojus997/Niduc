
class Receiver:
    def __init__(self):
        self.request = 1
        self.signal = {1, 0, 0, 0, 0}

    def setRequest(self, value):
        self.request = value

    def parity_decode(self):
        parity = 0
        for i in range(len(self.signal)):
            parity += self.signal[i]
        if parity % 2:
            return 1
        else:
            return 0

    def set_signal(self, signal):
        self.signal = signal

    def parity_check(self):
        parity = 0
        for x in self.signal:
            parity += x
        if parity % 2 == 0:
            self.setRequest(0)
            print("dobrze")
            return  # dobrze
        else:
            self.setRequest(1)
            print("blad")
            return  # blad w przesyle

    def get_request(self):
        return self.request

