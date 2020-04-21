import random


class Canal:
    def __init__(self):
        self.noise_percentage = 101
        while self.noise_percentage > 100 or self.noise_percentage < 0:
            self.noise_percentage = int(input("podaj % zagłuszenia"))
        self.signal = []
        random.seed()

    def set_signal(self, signal):
        self.signal = signal

    def noise(self):
        for i in range(len(self.signal)):
            if random.random() < float(self.noise_percentage/100):
                if self.signal[i] == 0:
                    self.signal[i] = 1
                else:
                    self.signal[i] = 0

    def send_through(self):
        return self.signal



