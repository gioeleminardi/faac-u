import logging
from faac_u import FaacU

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.WARNING)
    faacu = FaacU()
    faacu.run()
