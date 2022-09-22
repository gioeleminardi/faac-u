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
        self._sequencer = Sequencer()
        self._modulator = Modulator(12, 2000)
        try:
            self._pluto = Pluto(self._modulator.sampling_rate)
            self._pluto.set_tx(int(334e3))
            self._pluto.set_rx(int(334e3))
        except Exception as ex:
            self._log.warning("No Pluto")
            self._pluto = None

    def run(self):
        for sequence in self._sequencer.sequences:
            pwm_code = self._modulator.encode_pwm(sequence)
            ask_signal = self._modulator.modulate_ask(pwm_code)
            if self._pluto is None:
                plt.plot(self._modulator.timeline, np.real(ask_signal))
                plt.show()
            else:
                for i in range(500):
                    self._pluto.send(ask_signal)
                time.sleep(7)
