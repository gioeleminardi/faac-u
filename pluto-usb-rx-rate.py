import numpy as np
import adi
import matplotlib.pyplot as plt
import time

sample_rate = 4e6  # Hz
center_freq = 100e6  # Hz

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate)  # filter cutoff, just set it to the same as sample rate
sdr.rx_lo = int(center_freq)

# for buff_size in range(1, 33):
sdr.rx_buffer_size = 1024 * 32  # this is the buffer the Pluto uses to buffer samples
recv_samples = 0

start_time = time.time()
for i in range(200):
    samples = sdr.rx()  # receive samples off Pluto
    recv_samples += len(samples)
end_time = time.time()

sps = recv_samples / (end_time - start_time)
print(
    f"SampleRate: {sdr.sample_rate} - Buffer: {sdr.rx_buffer_size} - Time: {(end_time - start_time)} - Throughput: {sps} sps ({sps / sdr.sample_rate * 100}%)")
time.sleep(0.5)
