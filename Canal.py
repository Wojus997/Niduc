import random


class Canal:
    def __init__(self):
        self.signal = [0, 1, 0, 1, 1, 0]
        random.seed()
        print(self.signal)

    def set_signal(self, signal):
        self.signal = signal

    def noise(self):
        for i in range(len(self.signal)):
            if random.random() > 0.5:
                if self.signal[i] == 0:
                    self.signal[i] = 1
                else:
                    self.signal[i] = 0
        print(self.signal)

    def send_through(self):
        return self.signal


a = Canal()
a.noise()
