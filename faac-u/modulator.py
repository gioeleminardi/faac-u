class Modulator(object):
    def __init__(self, symbols, samples, baseband_fc=38e3, sampling_rate=2.1e6):
        self._symbols = symbols
        self._samples = samples
        self._baseband_fc = baseband_fc
        self._sampling_rate = sampling_rate

    @property
    def symbols(self):
        return self._symbols

    @property
    def samples(self):
        return self._samples

    @property
    def baseband_fc(self):
        return self._baseband_fc

    @property
    def sampling_rate(self):
        return self._sampling_rate
