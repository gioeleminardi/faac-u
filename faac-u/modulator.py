import numpy as np


class Modulator(object):
    def __init__(self, symbols, samples, baseband_fc=38e3, sampling_rate=2.1e6):
        self._symbols = symbols
        self._samples = samples
        self._baseband_fc = baseband_fc
        self._sampling_rate = sampling_rate
        self._dt = 1 / self._sampling_rate
        self._symbol_duration = self._samples * self._dt
        self._symbol_t = np.arange(0, self._symbol_duration, self._dt)
        self._max_duration = self._symbols * self._symbol_duration
        self._timeline = np.arange(0, self._max_duration, self._dt)

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

    def encode_pwm(self, bit_sequence):
        zero = 0.33
        one = 0.66
        zero_pwm = self._symbol_t % self._symbol_duration >= self._symbol_duration * zero
        one_pwm = self._symbol_t % self._symbol_duration >= self._symbol_duration * one
        pwm_sig = np.zeros(self._symbols * self._samples)
        i = 0
        for bit in bit_sequence:
            out_sig_idx = i * self._samples
            pwm_sig[out_sig_idx:out_sig_idx + self._samples] = zero_pwm if bit == 0 else one_pwm
            i += 1
        return pwm_sig

    def modulate_ask(self, signal):
        return np.exp(2.0j * np.pi * self._baseband_fc * self._timeline) * signal
