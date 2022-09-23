import logging
from faac_u import FaacU

sample_rate = 4e6  # Hz
center_freq = 333.8e6  # Hz
signal_carrier = 67e3  # Hz
symbols = 13
symbol_duration = 0.000990
tx_gain = -10

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
