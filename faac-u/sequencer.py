class Sequencer(object):
    def __init__(self, bits=12):
        self._bits = bits
        self._sequences = []
        sequence = [None] * self._bits
        self._generate(sequence, 0)

    @property
    def sequences(self):
        return self._sequences

    def print(self):
        for sequence in self._sequences:
            print(sequence)

    def _generate(self, sequence, idx):
        if idx == self._bits:
            self._sequences.append(sequence.copy())
            return
        sequence[idx] = 0
        self._generate(sequence, idx + 1)
        sequence[idx] = 1
        self._generate(sequence, idx + 1)
