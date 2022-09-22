import adi


class Pluto(object):
    def __init__(self, sample_rate: int, uri="ip:192.168.2.1"):
        self._uri = uri
        self._sample_rate = sample_rate
        self._sdr = adi.Pluto(uri)
        self._sdr.sample_rate = self._sample_rate

    def set_tx(self, carrier: int, tx_gain=-50, repeat=False):
        self._sdr.tx_rf_bandwidth = self._sample_rate  # filter cutoff, just set it to the same as sample rate
        self._sdr.tx_lo = carrier
        self._sdr.tx_hardwaregain_chan0 = tx_gain  # Increase to increase tx power, valid range is -90 to 0 dB
        self._sdr.tx_cyclic_buffer = repeat

    def set_rx(self, carrier: int):
        self._sdr.rx_rf_bandwidth = self._sample_rate
        self._sdr.gain_control_mode_chan0 = "slow_attack"
        self._sdr.rx_lo = carrier

    def send(self, complex_signal):
        self._sdr.tx(complex_signal)
