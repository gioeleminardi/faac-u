import time

import adi
import matplotlib.pyplot as plt
import numpy as np

from sequencer import Sequencer
from modulator import Modulator

sequencer = Sequencer()
modulator = Modulator(12, 2000)
pwm_code = modulator.encode_pwm(sequencer.sequences[0])
ask_signal = modulator.modulate_ask(pwm_code)
plt.plot(modulator.timeline, np.real(ask_signal))
plt.show()
