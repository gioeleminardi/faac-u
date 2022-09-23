import adi


class Pluto(object):
    def __init__(self, sample_rate, uri="ip:192.168.2.1"):
        self._uri = uri
        self._sample_rate = sample_rate
        self._sdr = adi.Pluto(uri)
        self._sdr.sample_rate = int(self._sample_rate)

    def set_tx(self, center_freq, tx_gain):
        self._sdr.tx_rf_bandwidth = self._sdr.sample_rate  # filter cutoff, just set it to the same as sample rate
        self._sdr.tx_lo = int(center_freq)
        self._sdr.tx_hardwaregain_chan0 = tx_gain  # Increase to increase tx power, valid range is -90 to 0 dB

    def set_rx(self, center_freq):
        self._sdr.rx_rf_bandwidth = self._sdr.sample_rate
        self._sdr.gain_control_mode_chan0 = "slow_attack"
        self._sdr.rx_lo = int(center_freq)

    def send(self, complex_signal):
        self._sdr.tx(complex_signal)
