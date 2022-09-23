# faac-u
PlutoSDR PWM over ASK sender

## Notes
- Encoder Carrier Frequency: ~70kHz
- RF Carrier Frequency: < 334 MHz
- Bit ONE encoding: 0->1 (33% DC)
- Bit ZERO encoding: 0->1 (66% DC)
- Maybe Decoder needs 3 packets to start decoding
- In the OnAir sequence, there is a "start bit" of type ONE (33% DC) 
- Between two consecutive sequences there are 10ms of idle
- A sequence is transmitted in ~12ms (including start bit)