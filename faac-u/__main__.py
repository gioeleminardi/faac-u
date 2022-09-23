import logging
from faac_u import FaacU

RF_Carrier = int(334e6)
TX_gain = -20
BB_Carrier = int(68e3)
sampling_rate = int(4e6)

symbol_duration = 0.000990  # seconds

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.WARNING)
    faacu = FaacU(rf_carrier=RF_Carrier, tx_gain=TX_gain, bb_carrier=BB_Carrier, sampling_rate=sampling_rate,
                  symbol_duration=symbol_duration)
    faacu.run()
