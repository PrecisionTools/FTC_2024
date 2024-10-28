import os
import numpy as np
import matplotlib.pyplot as plt
from adi import ad4080

basedir = os.getcwd()
print(basedir)

adc_ip = 'ip:10.10.1.120'
output_file = 'ADC_capture_as_PWL.txt'
capture_time = 5e-3

my_adc = ad4080(uri=adc_ip)#, device_name="ad4080")
fs = my_adc.sampling_frequency                  # Get sampling rate configured in ADC
Nsamples = np.clip(capture_time*fs, 0, 4e6)     # Limit number of samples to 4M
my_adc.rx_buffer_size = int(Nsamples)

bits = 20
MS = 2**(bits - 1)
FS = 2**bits - 1
ts = 1/float(fs)


my_adc.rx_destroy_buffer()
code = my_adc.rx()     # Collect data
code = np.array(code, dtype = float)
code = -code / MS    # Sign inversion because the ADC has an inverting amplifier.

time = np.arange(0, Nsamples*ts, ts)

#code = np.array(code, dtype = float)
 

plt.plot(time, code)
plt.show()

pfile = open(output_file, 'w')
for i in range(len(time)):
    pfile.write('%e, %e\n' % (time[i], code[i]))
pfile.close()


