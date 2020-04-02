class Receiver:
    def __int__(self, signal):
        self.signal = signal

    def parity_decode(self):
        parity = 0
        for i in range(len(self.signal)):
            parity += self.signal[i]
        if parity % 2:
            return 1
        else:
            return 0




