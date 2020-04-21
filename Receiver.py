def xor(a, b):
    if int(a) == int(b):
        return 0
    else:
        return 1


class Receiver:
    def __init__(self):
        self.request = 1
        self.signal = []
        self.crc = []

    def setRequest(self, value):
        self.request = value

    def set_crc(self, crc):
        self.crc = crc

    def parity_decode(self):
        parity = 0
        for i in range(len(self.signal)):
            parity += self.signal[i]
        if parity % 2:
            return 1
        else:
            return 0

    def crc_decode(self):
        check_sum = self.signal.copy()
        for i in range(0, len(self.signal) - len(self.crc) + 1):
            if check_sum[i] == 1:
                for u in range(0, len(self.crc)):
                    check_sum[u + i] = xor(check_sum[u + i], self.crc[u])
        print("crc chech_sum = ")
        print(check_sum)
        print("\n")
        for i in range(0, len(check_sum)):
            if check_sum[i] == 1:
                return
        self.setRequest(0)

    def set_signal(self, signal):
        self.signal = signal

    def parity_check(self):
        parity = 0
        for x in self.signal:
            parity += x
        if parity % 2 == 0:
            self.setRequest(0)
            print("end")
            return  # dobrze
        else:
            self.setRequest(1)
            print("request")
            return  # blad w przesyle

    def get_request(self):
        return self.request
