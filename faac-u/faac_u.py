import time

import matplotlib.pyplot as plt
import numpy as np
import logging

from pluto import Pluto
from sequencer import Sequencer
from modulator import Modulator


class FaacU(object):
    def __init__(self, rf_carrier: int, bb_carrier: int, sampling_rate: int, symbol_duration, tx_gain=-20):
        self._log = logging.getLogger(__name__)
        self._rf_carrier = rf_carrier
        self._tx_gain = tx_gain
        self._bb_carrier = bb_carrier
        self._symbol_duration = symbol_duration
        self._sampling_rate = sampling_rate
        self._sequencer = Sequencer(bits=13)
        self._modulator = Modulator(symbols=self._sequencer.bits, symbol_duration=self._symbol_duration,
                                    baseband_fc=self._bb_carrier, sampling_rate=self._sampling_rate)
        try:
            self._pluto = Pluto(int(self._modulator.sampling_rate))
            self._pluto.set_tx(self._rf_carrier, self._tx_gain)
            self._pluto.set_rx(self._rf_carrier)
        except Exception as ex:
            self._log.warning(f"No Pluto: {ex}")
            self._pluto = None

    def run(self):
        for sequence in self._sequencer.sequences:
            if sequence == [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]:
                pwm_code = self._modulator.encode_pwm(sequence)
                ask_signal = self._modulator.modulate_ask(pwm_code)
                if self._pluto is None:
                    plt.plot(self._modulator.timeline, np.real(ask_signal))
                    plt.show()
                else:
                    self._log.warning('sending')
                    for i in range(100):
                        self._pluto.send(ask_signal * (2 ** 14))
                        time.sleep(0.01)
