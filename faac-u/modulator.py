import numpy as np


class Modulator(object):
    def __init__(self, sample_rate, signal_carrier, symbols, symbol_duration):
        self._sample_rate = sample_rate
        self._signal_carrier = signal_carrier
        self._symbols = symbols
        self._symbol_duration = symbol_duration

        self._dt = 1 / self._sample_rate
        self._samples = np.floor(self._symbol_duration / self._dt)
        self._zero_dc = 0.33
        self._one_dc = 1 - self._zero_dc
        self._symbol_timeline = np.arange(0, self._symbol_duration, self._dt)
        self._zero_pwm_signal = self._symbol_timeline % self._symbol_duration >= self._symbol_duration * self._zero_dc
        self._one_pwm_signal = self._symbol_timeline % self._symbol_duration >= self._symbol_duration * self._one_dc
        self._timeline = np.arange(0, self._symbols * self._symbol_duration, self._dt)
        self._baseband_signal = 0.5 * np.exp(2.0j * np.pi * self._signal_carrier * self._timeline)

    @property
    def symbols(self):
        return self._symbols

    @property
    def samples(self):
        return self._samples

    @property
    def signal_carrier(self):
        return self._signal_carrier

    @property
    def sample_rate(self):
        return self._sample_rate

    @property
    def timeline(self):
        return self._timeline

    def encode_pwm(self, sequence):
        encoded_sequence = np.zeros(self._symbols * int(self._samples))
        idx = 0
        for symbol in sequence:
            encoded_sequence_idx = idx * int(self._samples)
            encoded_sequence[encoded_sequence_idx:encoded_sequence_idx + int(
                self._samples)] = self._zero_pwm_signal if symbol == 0 else self._one_pwm_signal
            idx += 1
        return encoded_sequence

    def modulate_ask(self, signal):
        return (self._baseband_signal * signal) * (2 ** 14)
