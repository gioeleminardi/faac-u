import time

import matplotlib.pyplot as plt
import numpy as np
import adi


def binary(symbols_, samples_):
    # symbols: no. of symbols to generate
    # sym_len: symbol duration or samples in a symbol
    rand_n_ = np.random.rand(symbols_)
    rand_n_[np.where(rand_n_ >= 0.5)] = 1
    rand_n_[np.where(rand_n_ < 0.5)] = 0
    return rand_n_


# Params
sample_rate = 4e6  # Hz
center_freq = 334e6  # Hz
signal_carrier = 70e3  # Hz
symbols = 13
symbol_duration = 0.000990
tx_gain = -30

dt = 1 / sample_rate
samples = np.floor(symbol_duration / dt)
symbol_timeline = np.arange(0, symbol_duration, dt)
zero = 0.33
one = 0.66
zero_pwm = symbol_timeline % symbol_duration >= symbol_duration * zero
one_pwm = symbol_timeline % symbol_duration >= symbol_duration * one

code = binary(symbols, int(samples))

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = sdr.sample_rate  # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = tx_gain  # Increase to increase tx power, valid range is -90 to 0 dB

t = np.arange(0, symbols * symbol_duration, dt)
signal = np.exp(2.0j * np.pi * signal_carrier * t)

pwm_sig = np.zeros(symbols * int(samples))

i = 0
for bit in code:
    out_sig_idx = i * int(samples)
    pwm_sig[out_sig_idx:out_sig_idx + int(samples)] = zero_pwm if bit == 0 else one_pwm
    i += 1

signal *= pwm_sig
signal *= 2 ** 14

for i in range(2000):
    sdr.tx(signal)  # transmit the batch of samples once
    time.sleep(0.02)
# plt.plot(t, np.real(signal))
# plt.plot(t, np.imag(signal))
# plt.grid()
# plt.show()
# time.sleep(10)
