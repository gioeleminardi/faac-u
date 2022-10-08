import time

import matplotlib.pyplot as plt
import numpy as np
import logging

from pluto import Pluto
from sequencer import Sequencer
from modulator import Modulator


class FaacU(object):
    def __init__(self, sample_rate, center_freq, signal_carrier, symbols, symbol_duration, tx_gain):
        self._log = logging.getLogger(__name__)

        self._sample_rate = sample_rate
        self._center_freq = center_freq
        self._signal_carrier = signal_carrier
        self._symbols = symbols
        self._symbol_duration = symbol_duration
        self._tx_gain = tx_gain

        self._sequencer = Sequencer(bits=self._symbols)

        self._modulator = Modulator(
            sample_rate=self._sample_rate,
            signal_carrier=self._signal_carrier,
            symbols=self._symbols,
            symbol_duration=self._symbol_duration
        )

        try:
            self._pluto = Pluto(sample_rate=self._sample_rate)
            self._pluto.set_tx(
                center_freq=self._center_freq,
                tx_gain=self._tx_gain
            )
        except Exception as ex:
            self._log.warning(f"No Pluto: {ex}")
            self._pluto = None

    def run(self):
        for sequence in self._sequencer.sequences:
            # if sequence == [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]:
            if sequence[0] == 1:
                encoded_sequence = self._modulator.encode_pwm(sequence)
                modulated_signal = self._modulator.modulate_ask(encoded_sequence)
                if self._pluto is None:
                    plt.plot(self._modulator.timeline, np.real(modulated_signal))
                    plt.plot(self._modulator.timeline, np.imag(modulated_signal))
                    plt.show()
                else:
                    self._log.warning('sending')
                    for i in range(3):
                        self._log.warning(f"Trying: {sequence}")
                        self._pluto.send(modulated_signal)
                        time.sleep(0.015)
