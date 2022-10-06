# faac-u

PlutoSDR PWM over ASK sender

## Notes

- Encoder Carrier Frequency: ~70kHz
- RF Carrier Frequency: ~333.85 MHz
- Bit ONE encoding: 0->1 (33% DC)
- Bit ZERO encoding: 0->1 (66% DC)
- Maybe Decoder needs 3 packets to start decoding
- In the OnAir sequence, there is a "start bit" of type ONE (33% DC)
- Between two consecutive sequences there are 10ms of idle
- A sequence is transmitted in ~12ms (including start bit)
- DUT PWR: -50dbFS

## snippet
```
sdr._ctrl.find_channel('altvoltage0',True).attrs['powerdown'].value = '1'
```
