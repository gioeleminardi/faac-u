import time

import matplotlib.pyplot as plt
import numpy as np
import logging

from pluto import Pluto
from sequencer import Sequencer
from modulator import Modulator


class FaacU(object):
    def __init__(self):
        self._log = logging.getLogger(__name__)
        self._sequencer = Sequencer(bits=13)
        self._modulator = Modulator(self._sequencer.bits, 2000)
        try:
            self._pluto = Pluto(int(self._modulator.sampling_rate))
            self._pluto.set_tx(int(334e6), -20)
            self._pluto.set_rx(int(334e6))
        except Exception as ex:
            self._log.warning(f"No Pluto: {ex}")
            self._pluto = None

    def run(self):
        for sequence in self._sequencer.sequences:
            # if sequence == [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1]:
            # if sequence == [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]:
            pwm_code = self._modulator.encode_pwm(sequence)
            ask_signal = self._modulator.modulate_ask(pwm_code)
            if self._pluto is None:
                plt.plot(self._modulator.timeline, np.real(ask_signal))
                plt.show()
            else:
                self._log.warning('sending')
                for i in range(100):
                    self._pluto.send(ask_signal * (2 ** 14))
