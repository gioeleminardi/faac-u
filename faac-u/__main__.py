import logging
from faac_u import FaacU

sample_rate = 4e6  # Hz
center_freq = 330e6  # Hz
signal_carrier = 19e3  # Hz
symbols = 13
symbol_duration = 0.000990
tx_gain = 0

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.WARNING)
    faacu = FaacU(
        sample_rate=sample_rate,
        center_freq=center_freq,
        signal_carrier=signal_carrier,
        symbols=symbols,
        symbol_duration=symbol_duration,
        tx_gain=tx_gain
    )
    faacu.run()
